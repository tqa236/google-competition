#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter

# For getting input from input.txt file
sys.stdin = open("runway_input.txt", "r")

# Printing the Output to output.txt file
sys.stdout = open("runway_output.txt", "w")


def func(t, n, m, initial_outfits, required_outfits):
    initial_changes = Counter(initial_outfits)
    last = initial_changes.copy()
    count = 0
    for required_outfit in required_outfits:
        curr = Counter(required_outfit)
        diff = last - curr
        for i in diff:
            if i in initial_changes:
                initial_i = initial_changes[i]
                initial_changes[i] = max(0, initial_changes[i] - diff[i])
                if initial_changes[i] == 0:
                    del initial_changes[i]
                    count += diff[i] - initial_i
                    # print(diff[i], initial_i)
            else:
                count += diff[i]
        # print(diff, count, initial_changes)
        last = curr
    return f"Case #{t+1}: {count}"


def main():
    num_test = int(parse_input())
    result = []
    for t in range(num_test):
        n, m = [int(i) for i in parse_input().split()]
        initial_outfits = [int(i) for i in parse_input().split()]
        required_outfits = []
        for r in range(n):
            required_outfits.append([int(i) for i in parse_input().split()])
        result.append(func(t, n, m, initial_outfits, required_outfits))
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
