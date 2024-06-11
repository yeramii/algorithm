"""
Pass
1. DFS - 53064KB 1324ms
2. BFS - 51724KB 1228ms

Tip
    - graph 생성 시,  V*V 배열을 통으로 만들지 말고, V행의 빈 리스트에 연결 정점만 추가해 줌
        . 통과        => [[] for _ in range(V+1)]
        . 메모리 초과  => [[0] * (V+1) for _ in range(V+1)]

이분 그래프 (Bipartite Graph)
    - 정의 : 집합이 두 개 있을 때, 인접한 노드끼리 서로 다른 집합에 넣을 수 있다면 이분 그래프
    - 풀이 : DFS로 탐색하면서 인접 노드는 다른 집합으로 표시해두고,
            인접 노드 중 현재 노드와 동일 집합을 발견하면 Fail
            -> 그래프가 끊어져 있을 수 있으므로, 모든 노드에서 탐색해야 한다.
"""
import sys
sys.stdin = open("input.txt")
sys.setrecursionlimit(10 ** 6)

def dfs(v, group=1):
    global ans
    if not ans: return

    visited[v] = group
    for w in graph[v]:
        if not visited[w]:
            dfs(w, -group)
        elif visited[w] == group:
            ans = False
            return

from collections import deque
def bfs(v, group=1):
    q = deque([v])
    visited[v] = group
    while q:
        v = q.popleft()
        for w in graph[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = -visited[v]
            elif visited[w] == visited[v]:
                return False
    return True

K = int(sys.stdin.readline())
for tc in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    visited = [0] * (V+1)   # A집합: 1, B집합: -1
    ans = True
    ### 1. DFS
    # for v in range(1, V+1):
    #     if not visited[v]:
    #         dfs(v)
    ### 2. BFS
    for v in range(1, V+1):
        if not visited[v]:
            ans = bfs(v)
            if not ans:
                break
    print("YES" if ans else "NO")
