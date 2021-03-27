#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def func_rev(array):
    n = len(array)
    cost = 0
    for i in range(n - 1):
        j = array.index(min(array[i:]))
        array = array[:i] + array[i : j + 1][::-1] + array[j + 1 :]
        cost += j - i + 1
    return cost


def func(t, n, c):
    if c < n - 1 or 2 * c > (n - 1) * (n + 2):
        return f"Case #{t+1}: IMPOSSIBLE"
    array = [None] * n
    c -= n - 1
    left = 0
    right = n - 1
    for i in range(1, n + 1):
        # print(i, c, array)
        if c >= (n - i):
            if i % 2 == 1:
                array[right] = i
                right -= 1
            else:
                array[left] = i
                left += 1
            c -= n - i
            # print("after", i, c, array)
        else:
            # print("break", i, c, left, right, array)
            if i % 2 == 0:
                # print(right, c)
                array[right - c] = i
                val = i + 1
                for j in range(right - c + 1, right + 1):
                    array[j] = val
                    val += 1
                for j in range(right - c - 1, left - 1, -1):
                    array[j] = val
                    val += 1
            else:
                array[left + c] = i
                val = i + 1
                for j in range(left + c - 1, left - 1, -1):
                    array[j] = val
                    val += 1
                for j in range(left + c + 1, right + 1):
                    array[j] = val
                    val += 1

            break
    return f"Case #{t+1}: " + " ".join([str(i) for i in array])


def main():
    num_test = int(parse_input())
    result = []
    for t in range(num_test):
        n, c = [int(i) for i in parse_input().split()]
        result.append(func(t, n, c))
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