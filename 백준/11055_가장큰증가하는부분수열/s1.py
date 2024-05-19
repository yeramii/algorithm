'''
Python3 - Pass

풀이 : 인덱스 0부터 i-1 중 A가 i에서보다 작을 때의 dp값 중 max + A[i] = dp[i]
    - LIS(Longest Increasing Subsequence)라는 유명한 DP문제라고 한다.
'''
import sys
sys.stdin = open('input.txt')

N = int(input())
A = list(map(int, input().split()))

dp = A[:]
for i in range(N):
    tmp = 0
    for j in range(i):
        if A[j] < A[i]:
            tmp = max(tmp, dp[j])
    dp[i] += tmp
print(max(dp))