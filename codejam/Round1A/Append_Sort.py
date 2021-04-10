#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def func(t, array):
    count = 0
    last = None
    for val in array:
        if last is None:
            last = val
            continue
        if int(last) < int(val):
            last = val
            continue
        same_last = int(last[: len(val)])
        int_val = int(val)
        if same_last < int_val:
            count += len(last) - len(val)
            last = val + "0" * (len(last) - len(val))
        elif same_last == int_val:
            plus_one = str(int(last) + 1)
            if plus_one.startswith(val):
                count += len(last) - len(val)
                last = plus_one
            else:
                count += len(last) - len(val) + 1
                last = val + "0" * (len(last) - len(val) + 1)
        else:
            count += len(last) - len(val) + 1
            last = val + "0" * (len(last) - len(val) + 1)
    return f"Case #{t+1}: {count}"


def main():
    num_test = int(parse_input())
    result = []
    for t in range(num_test):
        n = int(parse_input())
        array = [i for i in parse_input().split()]
        result.append(func(t, array))
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