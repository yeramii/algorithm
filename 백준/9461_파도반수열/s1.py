"""
Python3 - Pass

풀이 : i-1과 i-5의 합
다른 풀이 : i-2와 i-3의 합
"""
import sys
sys.stdin = open('input.txt')

T = int(input())
lstN = [int(input()) for _ in range(T)]
ans = [1] * max(lstN)
ans[3] = 2
ans[4] = 2
if max(lstN) > 5:
    for i in range(5, max(lstN)):
        ans[i] = ans[i-1] + ans[i-5]
for n in lstN:
    print(ans[n-1])