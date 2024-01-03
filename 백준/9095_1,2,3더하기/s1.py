'''
Python3 - Pass

풀이 : 1번 계산하고 쓰려고 max_n을 구해서 했는데, 문제에 최대가 11이라고 나와 있었음
    -> 문제 잘 읽자
'''
import sys
sys.stdin = open('input.txt')

T = int(input())
n = []
for _ in range(T):
    n.append(int(input()))

max_n = max(n)
ans = [0, 1, 2, 4]
if max_n > 3:
    ans += [0] * (max_n-3)
    for i in range(4, max_n+1):
        ans[i] = ans[i-1] + ans[i-2] + ans[i-3]

for i in range(T):
    print(ans[n[i]])