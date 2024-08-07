"""
Pass
bfs 보다는 dijkstra가 조금 더 메모리/시간 효율적

1. bfs
    - 찾아보고 bfs로 변경한 풀이 (deque)
    - deque에 append(), appendleft()를 달리 써서 heapq처럼 구현함
        . 먼저 검사해야 하는 것을 appendleft()
2. dijkstra
    - deque를 heapq로 바꿈
3. dfs
    - 처음 풀이
"""
import sys
sys.stdin = open("input.txt")

C, R = map(int, input().split())
arr = [input() for _ in range(R)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
visited = [[False] * C for _ in range(R)]

# 1. bfs - 34072KB 84ms
from collections import deque

def bfs():
    q = deque()
    q.append([0, 0, 0])
    while q:
        cost, r, c = q.popleft()
        if r == R - 1 and c == C - 1:
            return cost
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if rr not in range(R) or cc not in range(C) or visited[rr][cc]: continue
            visited[rr][cc] = True
            if arr[rr][cc] == "1":
                q.append([cost + 1, rr, cc])
            else:
                q.appendleft([cost, rr, cc])
# ans = bfs()
# print(ans)

# 2. dijkstra - 33188KB 72ms
import heapq

def dijkstra():
    q = []
    heapq.heappush(q, [0, 0, 0])
    while q:
        cost, r, c = heapq.heappop(q)
        if r == R-1 and c == C-1:
            return cost
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if rr not in range(R) or cc not in range(C) or visited[rr][cc]: continue
            visited[rr][cc] = True
            if arr[rr][cc] == "1":
                heapq.heappush(q, [cost + 1, rr, cc])
            else:
                heapq.heappush(q, [cost, rr, cc])
# ans = dijkstra()
# print(ans)


# 3. dfs - 시간 초과
def dfs(visited, r, c, cnt):
    global ans
    if cnt >= ans:
        return
    if r == R-1 and c == C-1:
        ans = cnt
        return
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        if rr not in range(R) or cc not in range(C): continue
        if visited[rr][cc]: continue
        visited[rr][cc] = True
        dfs(visited, rr, cc, cnt + int(arr[rr][cc]))
        visited[rr][cc] = False
ans = R + C - 3
# dfs(visited, 0, 0, 0)
# print(ans)