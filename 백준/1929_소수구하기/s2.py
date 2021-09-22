import sys
sys.stdin = open('input.txt')

M, N = map(int, input().split())

if M < 3:
    print(2)
    M = 3

memo = [0] * (N + 1)
memo[0] = 1
memo[1] = 1

for i in range(2, M):
    if not memo[i]:
        for j in range(i, N + 1):
            if not memo[j] and not (j % i):
                memo[j] = 1

for i in range(M, N + 1):
    if not memo[i]:
        print(i)
        memo[i] = 1
        for j in range(i + 1, N + 1):
            if not memo[j] and not j % i:
                memo[j] = 1

'''
[에라토스테네스의 체]

N+1 크기의 True로 이뤄진 리스트를 만들고, 2부터 1씩 증가하며 배수를 False로 바꾼다. 

'''