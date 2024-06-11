"""
Pass - 61480KB 2424ms

다른 사람의 풀이 참고. DFS는 보통 재귀 구조 사용
"""
import sys
sys.stdin = open("input.txt")
sys.setrecursionlimit(10 ** 6)

def dfs(i):
    global cnt
    visited[i] = 1
    cycle.append(i)
    if visited[child[i]]:
        if child[i] in cycle:
            cnt -= len(cycle[cycle.index(child[i]):])
        return
    else:
        dfs(child[i])

for _ in range(int(input())):
    n = int(input())
    child = [0] + list(map(int, input().split()))
    visited = [0] * (n+1)
    cnt = n
    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(cnt)