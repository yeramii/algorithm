"""
Python3 - Pass

풀이 : dp에 해당 계단을 밟았을 때의 최댓값을 저장 (배열 1개로 점화식 완성)
주의 : N은 300이하의 자연수이므로, 1 또는 2일 때를 따로 분기해야 함
"""
import sys
sys.stdin = open('input.txt')

N = int(input())
scores = [int(input()) for _ in range(N)]

dp = [0] * N    # 각 칸을 밟을 때의 최댓값을 저장
if N <= 2:
    print(sum(scores))
else:
    dp[0] = scores[0]
    dp[1] = scores[0] + scores[1]
    dp[2] = max(scores[0] + scores[2], scores[1] + scores[2])
    for i in range(3, N):
        dp[i] = max(dp[i-2] + scores[i], dp[i-3] + scores[i-1] + scores[i])
    print(dp[N-1])