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