#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter

# # For getting input from input.txt file
# sys.stdin = open("weak_typing_chapter_2_input.txt", "r")

# # Printing the Output to output.txt file
# sys.stdout = open("weak_typing_chapter_2_output.txt", "w")

MOD = 1000000007


def func(t, array):
    total_count = 0
    hand = None
    char_to_hand = {"X": "left", "O": "right"}
    hand_to_char = {"left": "X", "right": "O"}
    last_F = None
    total_switch = []
    for index, val in enumerate(array):
        if val in "OX":
            if not hand:
                hand = char_to_hand[val]
            else:
                if val != hand_to_char[hand]:
                    if last_F is None:
                        total_count = total_switch[-1] + index
                    else:
                        total_count = total_switch[-1] + last_F
                    hand = char_to_hand[val]
            last_F = None
        else:
            if last_F is None:
                last_F = index
        total_switch.append(total_count)
        # print(index, total_switch[-1])
    result = sum(total_switch) % MOD
    return f"Case #{t+1}: {result}"


def main():
    num_test = int(parse_input())
    result = []
    for t in range(num_test):
        n = int(parse_input())
        array = parse_input()
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
