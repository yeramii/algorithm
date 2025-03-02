"""
Bellman-Ford algorithm
    - dijkstra와 달리 음의 가중치를 포함한 graph의 최단 거리를 구하는 알고리즘
    - 모든 정점에 대해 V-1번의 반복을 통해 가능한 모든 경로를 탐색하여 정확한 답을 구함
    - 동작 원리
        . 음의 사이클이 없고 정점이 V개인 그래프에서,
          한 정점에서 출발한 다른 정점까지의 최단 경로는 많아봐야 V-1개의 간선을 지난다.
          (즉, 한 번 지난 정점은 지나지 않는다.)
        . 따라서, 모든 정점에 대해 V-1 번의 반복을 통해 가능한 모든 경로를 탐색하여 정확한 답을 내도록 한다.
    - [참고] https://4legs-study.tistory.com/26?category=886581
"""
import sys
sys.stdin = open("input.txt")
from collections import defaultdict
from heapq import heappop, heappush


def check_wormholes():
    global graphs, wormhole

    for start, end in wormhole:
        t = graphs[start][end]
        # 32%에서 시간초과 나서 추가해봄 (해도 똑같)
        is_possible = False
        for d in graphs.values():
            if start in d.keys():
                is_possible = True
                break
        if not is_possible:
            continue
        # s -> e로 시작해서 다시 s로 왔을 때, t가 0보다 작으면 True 반환
        q = [(t, end)]  # (time, node)
        while q:
            t, s = heappop(q)
            if s == start:
                break
            for e, delay in graphs[s].items():
                heappush(q, (t+delay, e))
        if t < 0:
            return True
    return False


TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split()) # 지점, 도로, 웜홀
    graphs = defaultdict(dict)      # start: {end: time}
    wormhole = []   # (start, end)
    for _ in range(M):
        S, E, T = map(int, input().split()) # 연결1, 연결2, 소요 시간
        if graphs[S].get(E):
            T = min(T, graphs[S][E])
        graphs[S][E] = T
        graphs[E][S] = T
    for _ in range(W):
        S, E, T = map(int, input().split()) # 시작, 도착, 줄어든 시간
        T *= -1
        if graphs[S].get(E):
            T = min(T, graphs[S][E])
        graphs[S][E] = T
        wormhole.append((S, E))

    ans = check_wormholes()
    print("YES" if ans else "NO")