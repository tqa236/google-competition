#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter
from string import ascii_uppercase


def func(t, text):
    text_len = len(text)
    vowel = ["A", "E", "I", "O", "U"]
    counter = Counter(text)
    most_common_vowel = None
    most_common_consonant = None
    num_vowels = 0
    num_consonants = 0
    for key, count in counter.most_common():
        if key in vowel:
            if not most_common_vowel:
                most_common_vowel = key
            num_vowels += count
        else:
            if not most_common_consonant:
                most_common_consonant = key
            num_consonants += count
    if not most_common_vowel:
        result = min(text_len, 2 * (text_len - counter[most_common_consonant]))
    elif not most_common_consonant:
        result = min(text_len, 2 * (text_len - counter[most_common_vowel]))
    else:
        switch_vowel = 2 * (num_vowels - counter[most_common_vowel]) + num_consonants
        switch_consonant = (
            2 * (num_consonants - counter[most_common_consonant]) + num_vowels
        )
        result = min(switch_vowel, switch_consonant)
    return f"Case #{t+1}: {result}"


def main():
    num_test = int(parse_input())
    result = []
    for t in range(num_test):
        text = parse_input()
        result.append(func(t, text))
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
