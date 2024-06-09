"""
Pass

1. BFS (반복문) - Pass : 38308KB 652ms
2. DFS (재귀) - Pass : 38412KB 668ms
    - sys.setrecursionlimit(10**6) <- RecursionError 피하기 위해 추가
    - RecursionError: 재귀와 관련된 에러
        . sys.getrecursionlimit() = 1000 : python이 정한 최대 재귀 깊이
3. DFS (반복문) - Fail : 시간 초과
"""
import sys
sys.stdin = open("input.txt")
# print(sys.getrecursionlimit())    # 1000

N, M = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u][v] = 1
    graph[v][u] = 1
visited = [0] * (N+1)

### 1. BFS 반복문 - 통과
def bfs(v):
    q = [v]
    visited[v] = 1
    while q:
        v = q.pop(0)
        for w in range(1, N+1):
            if graph[v][w] and not visited[w]:
                q.append(w)
                visited[w] = 1

### 2. DFS 재귀 - recursion limit 늘린 후 통과 (아니면 RecursionError 발생)
sys.setrecursionlimit(10**6)
def dfs(v):
    visited[v] = 1
    for w in range(1, N+1):
        if graph[v][w] and not visited[w]:
            dfs(w)

cc = 0
for i in range(1, N+1):
    if not visited[i]:
        # bfs(i)
        dfs(i)
        cc += 1
    if sum(visited[1:]) == N: break
print(cc)

### 3. DFS - 반복문 -> 시간 초과
# def dfs(v):
#     q = [v]
#     while q:
#         v = q.pop()
#         visited[v] = 1
#         for w in range(1, N+1):
#             if graph[v][w] and not visited[w]:
#                 q.append(w)
