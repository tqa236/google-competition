#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter
from typing import overload
import numpy as np

# For getting input from input.txt file
sys.stdin = open("valet_parking_chapter_1_input.txt", "r")

# Printing the Output to output.txt file
# sys.stdout = open("valet_parking_chapter_1_output.txt", "w")


def best_up(r, c, k, array, baseline):
    np_array = np.array(array, dtype=np.int8)
    # np_array = np.concatenate(
    #     (np_array, np.zeros((1000, c), dtype=np.int8)), axis=0, dtype=np.int8
    # )
    # np_array = np.concatenate(
    #     (np_array, np.zeros((baseline, c), dtype=np.int8)), axis=0, dtype=np.int8
    # )
    cumsum = np_array.cumsum(axis=0)
    best = baseline
    # print(cumsum)
    # print(k)
    for i in range(1, baseline):
        # print(k + i - 2, cumsum[k + i - 2, :])
        # print(cumsum[k + i - 2, :] - k + 1)
        overflow = np.maximum(0, cumsum[min(r - 1, k + i - 2), :] - k + 1)
        # print("overflow", overflow)
        curr = np.maximum(overflow, np_array[min(r - 1, k + i - 1), :])
        best = min(best, i + np.count_nonzero(curr))
        if best == 0 or i > baseline:
            return best
        # print(curr)
        # print(i, best, curr)
        # print(i, np.maximum(0, k - cumsum[k + i - 1, :]))
    # print("best", best)
    return best


def func(t, r, c, k, array):
    baseline = sum(array[k - 1])
    if baseline == 0:
        return f"Case #{t+1}: 0"
    print("baseline", baseline)

    best = min(
        baseline,
        best_up(r, c, k, array, baseline),
        best_up(r, c, r + 1 - k, array[::-1], baseline),
    )

    return f"Case #{t+1}: {best}"


def main():
    num_test = int(parse_input())
    result = []
    for t in range(num_test):
        r, c, k = [int(i) for i in parse_input().split()]
        array = []
        for i in range(r):
            array.append([1 if i == "X" else 0 for i in parse_input()])
        result.append(func(t, r, c, k, array))
    print("\n".join(map(str, result)))


# region fastio

# BUFSIZE = 8192


# class FastIO(IOBase):
#     newlines = 0

#     def __init__(self, file):
#         self._fd = file.fileno()
#         self.buffer = BytesIO()
#         self.writable = "x" in file.mode or "r" not in file.mode
#         self.write = self.buffer.write if self.writable else None

#     def read(self):
#         while True:
#             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
#             if not b:
#                 break
#             ptr = self.buffer.tell()
#             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
#         self.newlines = 0
#         return self.buffer.read()

#     def readline(self):
#         while self.newlines == 0:
#             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
#             self.newlines = b.count(b"\n") + (not b)
#             ptr = self.buffer.tell()
#             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
#         self.newlines -= 1
#         return self.buffer.readline()

#     def flush(self):
#         if self.writable:
#             os.write(self._fd, self.buffer.getvalue())
#             self.buffer.truncate(0), self.buffer.seek(0)


# class IOWrapper(IOBase):
#     def __init__(self, file):
#         self.buffer = FastIO(file)
#         self.flush = self.buffer.flush
#         self.writable = self.buffer.writable
#         self.write = lambda s: self.buffer.write(s.encode("ascii"))
#         self.read = lambda: self.buffer.read().decode("ascii")
#         self.readline = lambda: self.buffer.readline().decode("ascii")


# sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()
