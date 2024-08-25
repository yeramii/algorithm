"""
Pass - 55708KB 476ms

LCS (Longest Common Subsequence, 최장 공통 부분 수열)
    - 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것의 길이를 찾음
    - 풀이 : 2차원 배열을 통한 DP
"""
import sys
sys.stdin = open("input.txt")

s1 = ' ' + input()
s2 = ' ' + input()
dp = [[0] * len(s2) for _ in range(len(s1))]

for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])
