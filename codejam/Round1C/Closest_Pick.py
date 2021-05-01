#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def func(t, n, k, array):
    array = sorted(set(array))
    # print(array)
    win_count = [0, 0]
    last = None
    for val in array:
        if last is None:
            last = val
            win_count = [max(win_count), val - 1]
        else:
            width = val - last
            curr_win = width // 2
            if curr_win > min(win_count):
                win_count = [max(win_count), curr_win]
            left = width - 1 - curr_win
            if left > min(win_count):
                win_count = [max(win_count), left]
            last = val
        # print(val, win_count)
    if array[-1] < k:
        curr_win = k - array[-1]
        if curr_win > min(win_count):
            win_count = [max(win_count), curr_win]
    # print(win_count)
    return f"Case #{t+1}: {sum(win_count)/k}"


def main():
    num_test = int(parse_input())
    result = []
    for t in range(num_test):
        n, k = [int(i) for i in parse_input().split()]
        array = [int(i) for i in parse_input().split()]
        result.append(func(t, n, k, array))
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