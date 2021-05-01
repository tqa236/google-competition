#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter


def split_str(s):
    source = []
    curr = ""
    for i in s:
        if not curr:
            curr = curr + i
        else:
            if curr[0] != i:
                source.append(curr)
                curr = i
            else:
                curr = curr + i
    if curr:
        source.append(curr)
    return source


def count_op(s, e, max_change, old):
    count = 0
    miss = len(e) - len(s)
    for i in e[len(s) :]:
        if i != old:
            max_change -= 2
            count += 3
            old = i
            if max_change < 0:
                return "IMPOSSIBLE"
        else:
            count += 1
        # print(s, e, miss, i, count)
    return count


def func(t, array):
    s, e = array
    if s == "0":
        if e == "0":
            return f"Case #{t+1}: 0"
        if e == "1":
            return f"Case #{t+1}: 1"
        goal = split_str(e)
        if len(goal) >= 3:
            return f"Case #{t+1}: IMPOSSIBLE"
        elif len(goal) == 2:
            if len(goal[0]) > 1:
                return f"Case #{t+1}: {len(goal[0]) + 2 + len(goal[1])}"
            else:
                return f"Case #{t+1}: {1 + len(goal[1])}"
        else:
            return f"Case #{t+1}: {len(e) + 2}"
    if s == "1":
        if e == "0":
            return f"Case #{t+1}: 1"
        if e == "1":
            return f"Case #{t+1}: 0"
        goal = split_str(e)
        if len(goal) >= 3:
            return f"Case #{t+1}: IMPOSSIBLE"
        elif len(goal) == 2:
            if len(goal[0]) > 1:
                return f"Case #{t+1}: {len(goal[0]) + 1 + len(goal[1])}"
            else:
                return f"Case #{t+1}: { len(goal[1])}"
        else:
            return f"Case #{t+1}: {len(e) + 1}"

    candidates = []
    source = split_str(s)

    for i in range(len(source)):
        curr = "".join(source[i:])
        if e.startswith(curr):
            # print(source, curr, e, i)
            count = count_op(curr, e, i, "0")
            if count is not "IMPOSSIBLE":
                candidates.append(count)
                # break

    not_s = "".join("0" if i == "1" else "1" for i in s)
    # print(not_s)
    source = split_str(not_s)
    source.pop(0)
    for i in range(len(source)):
        curr = "".join(source[i:])
        if e.startswith(curr):
            # print(source, curr, e)
            count = count_op(curr, e, i, "1")
            if count is not "IMPOSSIBLE":
                candidates.append(count + 1)
                # break
    if candidates:
        return f"Case #{t+1}: {min(candidates)}"
    return f"Case #{t+1}: IMPOSSIBLE"


def main():
    num_test = int(parse_input())
    result = []
    for t in range(num_test):
        array = [i for i in parse_input().split()]
        result.append(func(t, array))
    print("\n".join(map(str, result)))
    # print(count_op("10", "100", 1))
    # print(count_op("10", "1000", 2))
    # print(count_op("10", "101", 3))
    # print(count_op("10", "101", 1))


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