"""
Python3 - Pass

풀이 : N, K table 채워서 규칙 발견
    -> 입력 인자 (K) 범위 분기 하는거 잊지 말기!
        문제의 조건 (10**9로 나눈 값 출력) 잊지 말기!
"""
import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
ans = [[1] * (N+1) for _ in range(K+1)]
if K < 2:
    print(ans[-1][-1])
else:
    for k in range(2, K+1):
        for n in range(N+1):
            ans[k][n] = sum(ans[k-1][:n+1])
    print(ans[-1][-1] % 10**9)