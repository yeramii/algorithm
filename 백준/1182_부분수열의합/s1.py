"""
Pass
1) 직접 구현 - 192968KB 1336ms
    : 배열을 넘겨주는게 너무 많아서 그런가보다~
2) combinations - 31120KB 320ms
"""
import sys
sys.stdin = open("input.txt")
from itertools import combinations

N, S = map(int, input().split())
nums = list(map(int, input().split()))

# 1) 직접 구현
def check_sum(chosen, start):
    global ans
    if chosen and sum(chosen) == S:
        ans.append(chosen[:])
    if start == N:
        return
    for nxt in range(start, N):
        chosen.append(nums[nxt])
        check_sum(chosen, nxt+1)
        chosen.pop()
    return
ans = []
check_sum([], 0)
print(len(ans))

# 2) combinations 사용
cnt = 0
for i in range(1, N+1):
    comb = combinations(nums, i)
    for c in comb:
        if sum(c) == S:
            cnt += 1
print(cnt)
