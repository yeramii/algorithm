import sys
sys.stdin = open('input.txt')


def f(k, ans):
    if k == M:
        print(ans.rstrip())
        return

    for i in range(N):
        if not u[i]:
            u[i] = 1
            f(k+1, ans + '{} '.format(p[i]))
            u[i] = 0


N, M = map(int, sys.stdin.readline().split())
p = [i for i in range(1, N+1)]
u = [0] * N
f(0, '')