"""
1)의 경우만 생각해서 틀렸다가, 1)과 2)의 최소를 구해야 한다는 것을 배움

정점 v1, v2를 경유하는 경우의 최단 경로
    = 모든 경우의 수 중에 최소값을 구함
        1) 1 -> v1 -> v2 -> N
        2) 1 -> v2 -> v1 -> N
"""
import sys
sys.stdin = open("input.txt")
from collections import defaultdict
from heapq import heappush, heappop

N, E = map(int, input().split())    # 정점, 간선
graph = defaultdict(dict)           # 양방향
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
v1, v2 = map(int, input().split())

INF = 1e9
def dijkstra(start):
    h = []
    dist = [INF for _ in range(N+1)]
    heappush(h, (0, start))
    dist[start] = 0

    while h:
        cost, node = heappop(h)
        if dist[node] < cost:
            continue
        for n, c in graph[node].items():
            cc = c + cost
            if cc < dist[n]:
                dist[n] = cc
                heappush(h, (cc, n))
    return dist

dist0 = dijkstra(1)
dist1 = dijkstra(v1)
dist2 = dijkstra(v2)
res = min(dist0[v1] + dist1[v2] + dist2[N], dist0[v2] + dist2[v1] + dist1[N])
print(res if res < INF else -1)
