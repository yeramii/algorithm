"""
Pass - 34720KB 1164ms

intention: Floyd-Warshall
mine: Dijkstra
"""
from collections import defaultdict
import heapq

n, m = map(int, input().split())
graphs = defaultdict(dict)
for _ in range(m):
    s, e, t = map(int, input().split())
    graphs[s][e] = t
    graphs[e][s] = t
max_num = 1000 * n

def find_first(s):   # 1
    ans_cost = [max_num] * (n+1)
    ans_first = ["-"] * (n+1)
    ans_cost[s] = 0
    q = []  # 2, 2, 2 / 1, 3, 3
    for v, cost in graphs[s].items():
        heapq.heappush(q, (cost, v, v))
        ans_cost[v] = cost
        ans_first[v] = v
    while q:
        cost, v, first = heapq.heappop(q)
        for w, c in graphs[v].items():
            if cost + c < ans_cost[w]:
                ans_cost[w] = cost + c
                ans_first[w] = first
                heapq.heappush(q, (cost+c, w, first))
    for i in ans_first[1:]:
        print(i, end=' ')
    print()

for i in range(1, n+1):
    find_first(i)