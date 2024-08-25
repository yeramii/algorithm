"""
Pass - 68380KB 688ms
: 시간 초과였었는데, sys.stdin.readline() 대신 input()을 써서 그랬음

Dijkstra
    - heapq에 넣을 때, (가중치, 정점) 순서의 튜플을 넣어야 함.
"""
import sys
sys.stdin = open("input.txt")
import heapq

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

dist = [float('inf')] * (V+1)
dist[K] = 0

q = [(0, K)]    # cost, vertex
heapq.heapify(q)
while q:
    d, u = heapq.heappop(q)
    if d > dist[u]:
        continue
    for w, v in graph[u]:
        dd = d + w
        if dd < dist[v]:
            dist[v] = dd
            heapq.heappush(q, (dd, v))

for i in range(1, V+1):
    if dist[i] == float('inf'):
        print("INF")
    else:
        print(dist[i])