"""
Pass
1) 내장함수 (from itertools import combinations) - 31120KB 44ms
2) comb 구현 - 31120KB 36ms
"""
import sys
from itertools import combinations
sys.stdin = open("input.txt")

def comb(arr, n):
    import copy
    result = []
    def generate(chosen, start):
        if len(chosen) == n:
            result.append(copy.deepcopy(chosen))
            return
        for i in range(start, len(arr)):
            chosen.append(arr[i])
            generate(chosen, i+1)
            chosen.pop()
    generate([], 0)
    return result

for line in sys.stdin.readlines():
    tc = line.split()
    if tc[0] == 0:
        break
    tc.pop(0)
    for lst in comb(tc, 6):
        print(' '.join(lst))
    print()
