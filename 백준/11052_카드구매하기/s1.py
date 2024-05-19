"""
Pass

dp문제인걸 못 알아챔 ㅠ
index가 의미있는 숫자라서 P(카드 점수 리스트)와 dp(카드 최대 가격 리스트)의 앞에 0을 붙임
"""

import sys
sys.stdin = open('input.txt')

N = int(input())
P = [0] + list(map(int, input().split()))

dp = [0] * (N+1)    # 카드를 N개 구매할 때의 최대 가격
for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + P[j])
print(dp[-1])
