import sys
sys.stdin = open('input.txt')

n = int(input())
ser = list(map(int, input().split()))
dp = ser[:]
for i in range(1, n):
    dp[i] = max(dp[i-1] + dp[i], dp[i])
print(max(dp))