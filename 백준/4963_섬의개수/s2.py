import sys
from collections import deque
sys.stdin = open("input.txt")

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]


def bfs(r, c, curr):
    arr[r][c] = curr
    q = deque([(r, c)]) # deque([  ]) 안에 (r, c)를 넣어야 함

    while q:
        (x, y) = q.popleft()
        for i in range(8):
            rr = x + dr[i]
            cc = y + dc[i]
            if rr in range(h) and cc in range(w) and arr[rr][cc] == 1:
                arr[rr][cc] = curr
                q.append((rr, cc))


while True:
    w, h = map(int, sys.stdin.readline().split())
    if not w and not h: break
    arr = []
    for _ in range(h):
        arr.append(list(map(int, sys.stdin.readline().split())))
    curr = 1
    for r in range(h):
        for c in range(w):
            if arr[r][c] != 1: continue
            curr += 1
            bfs(r, c, curr)
    print(curr - 1)
