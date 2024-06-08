"""
Pass
s1 - 109152KB 1096ms
s2 - 31120KB 1408ms
"""
import sys
sys.stdin = open("input.txt")

N = int(input())
if N == 1:
    pass
else:
    ans = [0] * (N+1)
    for i in range(2, int(N ** 0.5)+1):
        while N != 1:
            if not N % i:
                N //= i
                ans[i] += 1
            else:
                break
        if N == 1: break
    else:
        ans[N] = 1
    for i, n in enumerate(ans):
        if n > 0:
            for _ in range(n): print(i)
