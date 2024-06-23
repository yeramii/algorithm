"""
Pass
1) bfs - 35672KB 468ms
2) dfs - 35436KB 320ms
"""
import sys
sys.stdin = open("input.txt")
from collections import deque   # for bfs
sys.setrecursionlimit(10 ** 6)  # for dfs

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, c, d = map(int, input().split())
    tree[p].append((c, d))
    tree[c].append((p, d))

def bfs(start):
    q = deque([(start, 0)])
    visited = [-1] * (n+1)
    visited[start] = 0
    while q:
        (c, d) = q.popleft()
        for (cc, dd) in tree[c]:
            if visited[cc] == -1:
                visited[cc] = d + dd
                q.append((cc, visited[cc]))
    return (visited.index(max(visited)), max(visited))

### 1) bfs
# v, _ = bfs(1)
# w, d = bfs(v)
# print(d)

def dfs(v):
    global visited
    for (c, d) in tree[v]:
        if visited[c] == -1:
            visited[c] = visited[v] + d
            dfs(c)

### 2) dfs
visited = [-1] * (n+1)
visited[1] = 0
dfs(1)
v = visited.index(max(visited))
visited = [-1] * (n+1)
visited[v] = 0
dfs(v)
print(max(visited))