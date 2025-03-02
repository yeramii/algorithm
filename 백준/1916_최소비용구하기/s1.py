"""
Pass - 121268KB 268ms

INF 잘못해서 작게 설정했을 때 37%에서 Fail
"""
import sys
sys.stdin = open("input.txt")
from collections import defaultdict
from heapq import heappush, heappop

N = int(input())
M = int(input())
INF = 1e5 * N       # 버스 최대 비용 * 도시 개수
graph = defaultdict(dict)
distance = [INF] * (N+1)
for _ in range(M):
    s, e, c = map(int, input().split())
    bf_c = graph[s].get(e, None)
    if bf_c != None:
        graph[s][e] = min(bf_c, c)
    else:
        graph[s][e] = c
start, end = map(int, input().split())

def dijkstra(node):
    q = []
    heappush(q, (0, node))
    distance[node] = 0

    while q:
        cost, city = heappop(q)
        if distance[city] < cost:
            continue

        for k, v in graph[city].items():
            nxt_cost = cost + v
            if nxt_cost < distance[k]:
                distance[k] = nxt_cost
                heappush(q, (nxt_cost, k))
dijkstra(start)
print(distance[end])
