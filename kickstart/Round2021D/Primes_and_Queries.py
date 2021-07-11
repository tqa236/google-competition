#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter

CACHES = {}
CACHE_VALS = {}


def get_degree(x, p):
    if x == 0:
        return 0
    if (x, p) in CACHES:
        return CACHES[(x, p)]
    degree = 0
    org_x = x
    while x % p == 0:
        degree += 1
        x = x // p
    CACHES[(org_x, p)] = degree
    return degree


def func(t, n, q, p, array, queries):
    answers = []
    updates = {}
    for query in queries:
        if query[0] == 1:
            _, pos, val = query
            pos = pos - 1
            array[pos] = val
            if pos in updates:
                for s_val in updates[pos]:
                    del CACHE_VALS[(pos, s_val, p)]
                del updates[pos]
        else:
            _, s, l, r = query
            answer = 0
            for i in range(l - 1, r):
                if (i, s, p) not in CACHE_VALS:
                    if array[i] % p == 0:
                        val = get_degree(array[i], p) * s
                    else:
                        val = (
                            get_degree(array[i] - array[i] % p, p)
                            + get_degree((array[i] % p), p)
                            + get_degree(s, p)
                        )
                    CACHE_VALS[(i, s, p)] = val
                    if i in updates:
                        updates[i].add(s)
                    else:
                        updates[i] = set([s])
                answer += CACHE_VALS[(i, s, p)]
            answers.append(answer)
    return f"Case #{t+1}: {' '.join(map(str, answers))}"


def main():
    num_test = int(parse_input())
    result = []
    for t in range(num_test):
        n, q, p = [int(i) for i in parse_input().split()]
        array = [int(i) for i in parse_input().split()]
        queries = []
        for j in range(q):
            queries.append([int(i) for i in parse_input().split()])
        result.append(func(t, n, q, p, array, queries))
    print("\n".join(map(str, result)))


# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
parse_input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()
