"""
Pass - 42204KB 112ms
"""
import sys
sys.stdin = open("input.txt")

N, S = map(int, input().split())
nums = list(map(int, input().split()))
ans = -1
tmp = nums[0]
s, e = 0, 0
while True:
    if tmp >= S:
        if ans == -1:
            ans = e - s + 1
        else:
            ans = min(ans, e-s+1)
        tmp -= nums[s]
        s += 1
        if s >= N: break
        if e < s: e = s
    else:
        e += 1
        if e >= N: break
        tmp += nums[e]
    if ans == 1:
        break
print(0 if ans == -1 else ans)