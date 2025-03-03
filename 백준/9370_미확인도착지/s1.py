"""
Pass - 186416KB 4552ms

print(*res) : res라는 list 원소들을 " "로 구분하여 print
"""
import sys
sys.stdin = open("input.txt")
from heapq import heappush, heappop

INF = 1e8
for tc in range(int(input())):
    n, m, t = map(int, input().split()) # 교차로 수, 도로 수, 목적지 후보 수
    s, g, h = map(int, input().split()) # 출발지, 지나간 도로 시작/끝
    graph = [[] for _ in range(n + 1)]  # (node, cost)
    for _ in range(m):
        a, b, d = map(int, input().split()) # a와 b 사이에 d의 양방향 도로
        graph[a].append([b, d])
        graph[b].append([a, d])
    cand = []
    for _ in range(t):
        cand.append(int(input()))

    def dijkstra(start, end):
        global n
        h = []
        heappush(h, (0, start))
        dist = [INF for _ in range(n + 1)]
        dist[start] = 0

        while h:
            cost, node = heappop(h)
            if dist[node] < cost:
                continue

            for nn, c in graph[node]:
                cc = c + cost
                if cc < dist[nn]:
                    dist[nn] = cc
                    heappush(h, (cc, nn))
        return dist[end]

    res = []
    for c in cand:
        route1 = dijkstra(s, g) + dijkstra(g, h) + dijkstra(h, c)
        route2 = dijkstra(s, h) + dijkstra(g, h) + dijkstra(g, c)
        if dijkstra(s, c) == min(route1, route2):
            res.append(c)
    res.sort()
    print(*res)
    # for r in res:
    #     print(r, end=' ')
    # print()