'''
Pass
    Python3 - 메모리 38676 KB, 시간 624 ms
    PyPy3 - 메모리 133152 KB, 시간 136 ms

[다른 사람 풀이]: DP = 점화식 세우기
'''
import sys
sys.stdin = open('input.txt')

X = int(input())
dp = [0] * (X+1)

for i in range(2, X+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[X])