"""
Pass - 38448KB 568ms

dfs를 while & stack 로 구현하려 했는데, 숫자 순서대로 출력되지 않음 -> 재귀 사용
"""
import sys
sys.stdin = open("input.txt")

N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    i, j = map(int, input().split())
    graph[i][j] = 1
    graph[j][i] = 1

visited_d = [0] * (N + 1)
visited_b = [0] * (N + 1)

def dfs(v):
    visited_d[v] = 1
    print(v, end=" ")
    for w in range(1, N+1):
        if graph[v][w] and not visited_d[w]:
            dfs(w)

def bfs(v):
    q = [v]
    while q:
        v = q.pop(0)
        if not visited_b[v]:
            visited_b[v] = 1
            print(v, end=' ')
            for w in range(1, N+1):
                if graph[v][w] and not visited_b[w]:
                    q.append(w)

dfs(V)
print()
bfs(V)