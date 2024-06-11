import sys
sys.stdin = open("input.txt")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

from collections import deque
def bfs(r, c):
    q = deque()
    q.append((r, c))    # 상하좌우 탐색의 대상 좌표 (해당 좌표는 이미 counted)
    arr[r][c] = 0
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            rr = x + dr[i]
            cc = y + dc[i]
            if rr not in range(N) or cc not in range(N):
                continue
            if arr[rr][cc] == 1:
                arr[rr][cc] = 0
                q.append((rr, cc))
                cnt += 1
    return cnt

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input())))
cnt = []
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            cnt.append(bfs(r, c))
cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)