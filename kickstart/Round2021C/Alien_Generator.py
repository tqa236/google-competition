#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter
import itertools

PRIMES = set([3])


def primeFactors(n):
    if n == 1:
        return Counter({})
    exponents = {}
    count = 0
    while n % 2 == 0:
        count += 1
        n = n // 2
    if count > 0:
        exponents[2] = count
    for i in PRIMES:
        count = 0
        while n % i == 0:
            count += 1
            n = n // i
        if count > 0:
            exponents[i] = count
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if i in exponents:
            continue
        count = 0
        while n % i == 0:
            count += 1
            n = n // i
        if count > 0:
            exponents[i] = count
        if count > 0:
            PRIMES.add(i)
    if n > 2:
        exponents[n] = 1
        PRIMES.add(n)
    # print(PRIMES)
    return Counter(exponents)


def product(keys, exponents):
    i = 1
    for key, exponent in zip(keys, exponents):
        i *= key ** exponent
    return i


def func(t, n):
    factors = primeFactors(n)
    if 2 in factors:
        del factors[2]
    keys = factors.keys()
    count = 1
    for val in factors.values():
        count *= val + 1

    return f"Case #{t+1}: {count}"


def main():
    num_test = int(parse_input())
    result = []
    for t in range(num_test):
        n = int(parse_input())
        result.append(func(t, n))
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