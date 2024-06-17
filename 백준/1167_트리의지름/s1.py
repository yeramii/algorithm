"""
Pass
    1) BFS - 76108KB 4704ms
    2) DFS - 71724KB 3268ms

다른 풀이 참고

* 트리 지름 공식
    : u-v가 지름이라고 할 때, 임의의 점에서 가장 먼 거리의 노드 y는 반드시 u 또는 v이다.
    따라서 y에서 가장 먼 노드와의 길이를 구하면 지름이다.
"""
import sys
sys.stdin = open("input.txt")
from collections import deque

V = int(input())
tree = [[] for _ in range(V+1)] # 2차원 리스트에 트리 저장
for _ in range(V):
    tmp = list(map(int, input().split()))
    par = tmp[0]
    idx = 1
    while tmp[idx] != -1:
        node, cost = tmp[idx], tmp[idx+1]
        tree[par].append((node, cost))
        idx += 2

## 1. bfs
def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [-1] * (V+1)
    visited[start] = 0
    res = [0, 0]    # start로부터 가장 먼 곳에 있는 노드와 거리 값

    while q:
        from_n, from_c = q.popleft()
        for to_n, to_c in tree[from_n]:
            if visited[to_n] == -1:
                dist = from_c + to_c
                q.append((to_n, dist))
                visited[to_n] = dist
                if res[1] < dist:
                    res[0] = to_n
                    res[1] = dist
    return res

# n, c = bfs(1)
# print(bfs(n)[1])

## 2. dfs
def dfs(node, cost):
    global visited
    for n, c in tree[node]:
        dist = cost + c
        if visited[n] == -1:
            visited[n] = dist
            dfs(n, dist)

visited = [-1] * (V+1)
visited[1] = 0
dfs(1, 0)
tmp = [0, 0]
for i in range(1, V+1):
    if visited[i] > tmp[1]:
        tmp[1] = visited[i]
        tmp[0] = i

visited = [-1] * (V+1)
visited[tmp[0]] = 0
dfs(tmp[0], 0)
print(max(visited))