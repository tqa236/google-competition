#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter

FIB0 = [1, 0]
FIB1 = [0, 1]

for i in range(2, 40):
    FIB0.append(FIB0[i - 1] + FIB0[i - 2])
    FIB1.append(FIB1[i - 1] + FIB1[i - 2])

# print(FIB0, FIB1)


def func(t, n, a, b, array):
    if len(array) == 1:
        array.append(0)
    for i in range(len(array) - 2):
        if array[i] == 0:
            continue
        if array[i] > array[i + 1]:
            left = (array[i] - array[i + 1]) % 2
            array[i + 2] += (array[i] - array[i + 1]) // 2
            array[i + 1] += left
            array[i] = 0
        else:
            array[i + 1] -= array[i]
            array[i + 2] += array[i]
            array[i] = 0
    #     print(i, array)
    # print(array)
    for i in range(len(FIB0)):
        val1 = FIB0[i]
        val2 = FIB1[i]
        if array[-2] + array[-1] <= val1 + val2 and array[-1] <= val2:
            return f"Case #{t+1}: {i + len(array) - 1}"


def main():
    num_test = int(parse_input())
    result = []
    for t in range(num_test):
        n, a, b = [int(i) for i in parse_input().split()]
        array = [int(i) for i in parse_input().split()]
        result.append(func(t, n, a, b, array))
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