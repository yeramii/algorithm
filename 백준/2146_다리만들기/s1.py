"""
Pass - 34148KB 1708ms

이중 BFS
1. land 별로 다를 숫자 부여 (2~)
2. land 별로 주위 land로 까지의 최단 경로 구함 -> land 수만큼 BFS 돌림
"""
import sys
sys.stdin = open("input.txt")
from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def paint_land(r, c):
    global arr
    q = deque([(r, c)])
    while q:
        (r, c) = q.popleft()
        if arr[r][c] == 1:
            arr[r][c] = land
            for i in range(4):
                rr = r + dr[i]
                cc = c + dc[i]
                if rr in range(N) and cc in range(N) and arr[rr][cc] == 1:
                    q.append((rr, cc))

land = 2
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            paint_land(r, c)
            land += 1

def find_route(land):
    q = deque([])
    dist = [[-1] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if arr[r][c] == land:
                q.append((r, c))
                dist[r][c] = 0
    while q:
        (r, c) = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if rr in range(N) and cc in range(N):
                if not arr[rr][cc] and dist[rr][cc] == -1:    # 바다고 아직 탐험한 적이 없다면
                    dist[rr][cc] = dist[r][c] + 1
                    q.append((rr, cc))
                elif arr[rr][cc] != 0 and arr[rr][cc] != land:   # 다른 섬이면
                    return dist[r][c]

ans = 100 ** 2
for l in range(2, land):
    ans = min(ans, find_route(l))
print(ans)