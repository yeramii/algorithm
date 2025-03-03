"""
Pass - 172696KB 944ms

(개선한 점)
- 시작은 항상 1이므로 dijkstra()는 한 번만 호출한 뒤, 결과 리스트를 재활용하면 됨
    -> 시간 절약
- wolf()의 2차원 배열 dist에서 첫 원소만 0으로 하고, 두 번째 원소는 INF 그대로 둬야 함!!
    -> 틀렸던 부분

(문제)
1~N 나무. 나무 사이 M개 양방향 오솔길.
- 여우 : 속도 x - x 일정
- 늑대 : 속도 2x - 0.5x 반복
여우가 늑대보다 빨리 도달할 나무 갯수?
"""
import sys
sys.stdin = open("input.txt")
from heapq import heappush, heappop

N, M = map(int, input().split())    # 나무, 오솔길
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, d = map(int, input().split()) # a와 b 나무 사이 d 길이의 오솔길
    graph[a].append([b, d])
    graph[b].append([a, d])
INF = 1e10

def fox():
    h = []
    heappush(h, (0, 1))
    dist = [INF for _ in range(N+1)]
    dist[1] = 0

    while h:
        cost, node = heappop(h)
        if dist[node] < cost:
            continue
        for n, c in graph[node]:
            cc = c + cost
            if cc < dist[n]:
                dist[n] = cc
                heappush(h, (cc, n))
    return dist

def wolf():
    h = []
    heappush(h, (0, 1, 0)) # cost, node, even(1이면 2, 0이면 0.5 였던 것.)
    dist = [[INF, INF] for _ in range(N + 1)]
    dist[1][0] = 0

    while h:
        cost, node, flag = heappop(h)
        if dist[node][flag] < cost:
            continue
        for n, c in graph[node]:
            cc = cost + (0.5 + flag*1.5) * c
            if cc < dist[n][(flag+1)%2]:
                dist[n][(flag+1)%2] = cc
                heappush(h, (cc, n, (flag+1)%2))
    return dist

res = 0
res_fox = fox()
res_wolf = wolf()
for i in range(2, N+1):
    if res_fox[i] < min(res_wolf[i]):
        res += 1
print(res)