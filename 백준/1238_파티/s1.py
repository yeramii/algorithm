"""
Pass
- graph를 list로 하는게 메모리/시간 효울적

1) graph is list -> 118588KB 1212ms
2) graph is defaultdict(dict) -> 122896KB 1096ms
"""
import sys
sys.stdin = open("input.txt")
from heapq import heappush, heappop
# from collections import defaultdict

N, M, X = map(int, input().split()) # 마을, 단방향 도로, 목적지 마을
graph = [[] for _ in range(N+1)]
# graph = defaultdict(dict)
for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))
    # graph[s][e] = t


INF = 1e6
def dijkstra(start, end):
    if start == end: return 0
    h = []
    h.append((0, start))
    dist = [INF for _ in range(N+1)]
    dist[start] = 0

    while h:
        cost, node = heappop(h)
        if dist[node] < cost:
            continue

        # for n, c in graph[node].items():
        for n, c in graph[node]:
            cc = c + cost
            if cc < dist[n]:
                dist[n] = cc
                heappush(h, (cc, n))
    return dist[end]

res = 0
for i in range(1, N+1):
    res = max(res, dijkstra(i, X) + dijkstra(X, i))
print(res)
