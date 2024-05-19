"""
Python3 - Pass (34972KB, 7568ms)
PyPy3 - Pass (111188KB, 204ms)

풀이 : dp에 최소 개수를 저장하며, 1부터 제곱근까지 모든 dp를 검사함
"""
import sys
sys.stdin = open('input.txt')

N = int(input())
dp = [i for i in range(N+1)]
for i in range(1, N+1):
    for j in range(1, 1 + int((i ** 0.5)//1)):
        dp[i] = min(dp[i], dp[i-j**2] + 1)
print(dp[-1])