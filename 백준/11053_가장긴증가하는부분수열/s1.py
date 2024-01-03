'''
Python3 - Pass

TC를 만들어가며 예외 케이스 찾아서 공식 완성

풀이 : 인덱스 0부터 i-1 중 A가 i에서보다 작을 때의 dp값 중 max + 1 = dp[i]
    - LIS(Longest Increasing Subsequence)라는 유명한 DP문제라고 한다.
'''
import sys
sys.stdin = open('input.txt')

N = int(input())
A = list(map(int, input().split()))

dp = [0] * N
dp[0] = 1
if N >= 2:
    for i in range(1, N):
        tmp = 0
        for j in range(i):
            if A[j] < A[i] and dp[j] > tmp:
                tmp = dp[j]
        dp[i] = tmp+1
print(max(dp))


# 기본 입력 이후를 아래와 같이 작성해도 됨 (다른 사람 풀이)
dp2 = [1] * N
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))