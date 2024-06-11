"""
Fail - 시간 초과

DFS로 실컷 풀다가 BFS로 해야 한다는 것을 깨달았다.. (깊이 들어가면 안되고, 주변을 하나씩 봐야 함)
반례 모음집 봤는데, 구현은 잘 되어 있음. 시간의 문제 !!
"""
import sys
sys.stdin = open("input.txt")
from collections import deque

C, R = map(int, input().split())
box = []
matured = []
is_perfect = True
for r in range(R):
    tmp = list(map(int, sys.stdin.readline().split()))
    for i, c in enumerate(tmp):
        if c == 1:
            matured.append((r, i))
        if c == 0:
            is_perfect = False
    box.append(tmp)

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def find_tomato(r, c):
    global box, visited
    visited[r][c] = 1
    q = deque([(r, c, 1)])
    while q:
        (x, y, day) = q.popleft()
        for i in range(4):
            rr = x + dr[i]
            cc = y + dc[i]
            if rr in range(R) and cc in range(C) and box[rr][cc] not in [1, -1] and not visited[rr][cc]:
                visited[rr][cc] = 1
                if box[rr][cc] == 0 or box[rr][cc] > day:
                    box[rr][cc] = day
                    q.append((rr, cc, day+1))

if len(matured) == C * R or is_perfect:
    print(0)
elif not matured:
    print(-1)
else:
    day = 1
    for (r, c) in matured:
        visited = [[0] * C for _ in range(R)]
        find_tomato(r, c)
    is_perfect = True
    for r in range(R):
        if 0 in box[r]:
            is_perfect = False
            break
        day = max(day, max(box[r]))
    if is_perfect:
        print(day)
    else:
        print(-1)