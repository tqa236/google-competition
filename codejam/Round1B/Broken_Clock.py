#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter
from itertools import permutations

REVERSE_TICK = 12 * 10 ** 10
HOUR = 30 * REVERSE_TICK
MIN = 6 * REVERSE_TICK
SECOND = 6 * REVERSE_TICK
WHOLE = 360 * REVERSE_TICK
PERMS = list(permutations([0, 1, 2]))


def func(t, array):
    n = 0
    # print([val % SECOND for val in array])
    for counter_s in range(60):
        for offset in range(3):
            new_array = [
                (val + counter_s * SECOND - array[offset] % SECOND) % WHOLE
                for val in array
            ]
            for perm in PERMS:
                hour_index, min_index, second_index = perm
                h = new_array[hour_index] // HOUR
                m = new_array[min_index] // MIN
                s = new_array[second_index] // SECOND
                n = new_array[second_index] % SECOND
                min = m * MIN + s * MIN // 60
                hour = h * HOUR + m * HOUR // 60 + s * HOUR // 3600
                # print(h, m, s)
                if (min, hour) != (new_array[min_index], new_array[hour_index]):
                    continue
                if h < 0 or h > 11 or m < 0 or m > 59 or s < 0 or s > 59:
                    continue
                return f"Case #{t+1}: {h} {m} {s} {n}"


def main():
    num_test = int(parse_input())
    result = []
    for t in range(num_test):
        array = [int(i) for i in parse_input().split()]
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