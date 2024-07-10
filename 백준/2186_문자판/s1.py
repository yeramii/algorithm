"""
DFS + memoization

1) Python3 - Fail : 시간 초과
2) PyPy3 - Pass : 124352KB 1012ms
"""
import sys
sys.stdin = open("input.txt")
N, M, K = map(int, input().split())
arr = [input() for _ in range(N)]
target = input()
cnt = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
memo = [[[-1 for _ in range(len(target))] for _ in range(M)] for _ in range(N)]

def dfs(r, c, i):
    global memo
    if memo[r][c][i] != -1:
        return memo[r][c][i]
    if i == len(target)-1:
        return 1
    cnt = 0
    for k in range(4):
        rr = r + dr[k]
        cc = c + dc[k]
        if rr not in range(N) and cc not in range(M): continue
        for j in range(1, K+1):
            rr = r + j * dr[k]
            cc = c + j * dc[k]
            if rr in range(N) and cc in range(M) and arr[rr][cc] == target[i+1]:
                cnt += dfs(rr, cc, i+1)
    memo[r][c][i] = cnt
    return cnt

cnt = 0
for r in range(N):
    for c in range(M):
        if arr[r][c] == target[0]:
            cnt += dfs(r, c, 0)
print(cnt)