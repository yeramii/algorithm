"""
Fail - 시간 초과

just DFS
"""
import sys
sys.stdin = open("input.txt")
N, M, K = map(int, input().split())
arr = [input() for _ in range(N)]
target = input()
cnt = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, i):
    global cnt
    if i == len(target)-1:
        cnt += 1
        return
    for k in range(4):
        rr = r + dr[k]
        cc = c + dc[k]
        if rr not in range(N) and cc not in range(M): continue
        for j in range(1, K+1):
            rr = r + j * dr[k]
            cc = c + j * dc[k]
            if rr in range(N) and cc in range(M) and arr[rr][cc] == target[i+1]:
                dfs(rr, cc, i+1)

for r in range(N):
    for c in range(M):
        if arr[r][c] == target[0]:
            dfs(r, c, 0)
print(cnt)