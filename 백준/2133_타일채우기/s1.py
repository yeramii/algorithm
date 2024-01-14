"""
Python3 - Pass

풀이 : 타일이 2n개일 때 unique한 2가지가 있음
    (힌트보고 4까지만 있는줄 알았는데 2n 마다 있다. -> 규칙을 확장하여 생각!)
"""
import sys
sys.stdin = open('input.txt')

N = int(input())
if N % 2:
    print(0)
else:
    N //= 2
    dp = [1] * (N+1)
    dp[1] = 3
    if N > 1:
        for i in range(2, N+1):
            dp[i] = dp[i-1] * 3
            for j in range(i-2, -1, -1):
                dp[i] += dp[j] * 2
    print(dp[-1])