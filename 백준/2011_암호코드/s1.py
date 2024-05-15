"""
Pass - 31120KB, 40ms

DP 문제는 역시 테이블 하나 만들고 채우는게 가장 효율적인 것 같다.
"""
import sys
sys.stdin = open('input.txt')

C = list(map(int, input()))
dp = [0] * (len(C) + 1) # 각 자리까지 왔을 때의 경우의 수
dp[0] = 1

if C[0] == 0:
    print(0)
else:
    for i in range(len(C)):
        if C[i] > 0:
            dp[i+1] += dp[i]
        if i > 0 and 10 <= C[i-1] * 10 + C[i] <= 26:
            dp[i+1] += dp[i-1]
    print(dp[-1] % 1000000)