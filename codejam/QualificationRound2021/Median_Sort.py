#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import math
from collections import Counter

# Run the test with: python interactive_runner.py python testing_tool.py 0 -- python Median_Sort.py


def func(n, CACHES):
    order = [-1] * n
    curr = [1, 2, 3]
    print("1 2 3")
    sys.stdout.flush()
    med = int(input())
    if med == -1:
        return -1
    CACHES["1 2 3"] = med
    curr = [j for j in curr if j != med]
    correct_order = list(range(1, n + 1))
    for i in range(4, n + 1):
        curr.append(i)
        curr_query = " ".join([str(j) for j in sorted(curr)])
        print(curr_query)
        sys.stdout.flush()
        med = int(input())
        if med == -1:
            return -1
        CACHES[curr_query] = med
        curr = [j for j in curr if j != med]
    curr = sorted(curr)
    min_index = curr[0]
    max_index = curr[1]
    order[min_index - 1] = 1
    order[max_index - 1] = n
    correct_order = [min_index, max_index]
    rest = sorted(set(range(1, n + 1)) - set(correct_order), reverse=True)
    while rest:
        value = rest.pop()
        low = 0
        high = len(correct_order) - 1
        median = int(math.ceil((low + high) / 2))
        while high - low > 1:
            curr = [correct_order[low], correct_order[median], value]
            curr_query = " ".join([str(j) for j in sorted(curr)])
            if curr_query in CACHES:
                med = CACHES[curr_query]
            else:
                print(curr_query)
                sys.stdout.flush()
                med = int(input())
                if med == -1:
                    return -1
                CACHES[curr_query] = med

            if med == value:
                high = median
            else:
                low = median
            median = int(math.ceil((low + high) / 2))
        correct_order.insert(median, value)

    print(" ".join([str(i) for i in correct_order]))
    sys.stdout.flush()
    s = int(input())
    return s


def main():
    t, n, q = [int(i) for i in input().split()]
    for i in range(t):
        s = func(n, CACHES={})
        sys.stdout.flush()
        if s == -1:
            break


if __name__ == "__main__":
    main()