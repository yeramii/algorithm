"""
Fail - 메모리 초과

DFS/BFS 쓰지 않고 생각한 풀이
"""
import sys
sys.stdin = open("input.txt")
from itertools import combinations

K = int(input())
for tc in range(K):
    V, E = map(int, input().split())
    graph = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u][v] = 1
        graph[v][u] = 1
    ans = "YES"
    for comb in combinations(range(1, V+1), 3):
        if graph[comb[0]][comb[1]] and graph[comb[1]][comb[2]] and graph[comb[0]][comb[2]]:
            ans = "NO"
            break
    print(ans)