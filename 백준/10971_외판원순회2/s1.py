"""
Pass - 31120KB 136ms
"""
import sys
sys.stdin = open("input.txt")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
ans = N * 10 ** 6

def dfs(v, cost, visited):
    global ans
    if cost >= ans: return
    if sum(visited) == N*(N+1)//2:
        tmp = arr[v][visited.index(1)]
        if tmp and cost + tmp < ans:
            ans = cost + tmp
            return
    for w in range(N):
        if not visited[w] and arr[v][w]:
            visited[w] = visited[v] + 1
            dfs(w, cost+arr[v][w], visited)
            visited[w] = 0

for i in range(N):
    visited[i] = 1
    dfs(i, 0, visited)
    visited[i] = 0
print(ans)