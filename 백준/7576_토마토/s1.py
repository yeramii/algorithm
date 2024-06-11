"""
Pass - 106760KB 2960ms

s2 (내가 한 풀이)와의 차이
    - s2에서는 토마토 1개에 큐 1개 할당 => 시간이 토마토 개수의 배수로 늘어남
    - s1에서는 모든 토마토를 1개의 큐에 넣고 진행

코드 강제 종료 : exit()
    - sys.exit()을 해도 되고, exit()을 해도 됨
    - exit(0) : 성공 종료
    - exit(1) : 실패 종료 => RuntimeError 발생 가능

"""
import sys
sys.stdin = open("input.txt")
from collections import deque

C, R = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(R)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
q = deque([])
ans = 0

# 토마토의 위치를 모두 넣음
for r in range(R):
    for c in range(C):
        if box[r][c] == 1:
            q.append([r, c])

def bfs():
    while q:
        (r, c) = q.popleft()
        for i in range(4):
            rr = r + dr[i]
            cc = c + dc[i]
            if rr in range(R) and cc in range(C) and box[rr][cc] == 0:
                box[rr][cc] = box[r][c] + 1
                q.append([rr, cc])
bfs()

for row in box:
    for a in row:
        if a == 0:
            print(-1)
            exit(0)     # 코드 강제 종료 (0: 성공, 1: 실패) -> 1은 runtime error 발생 가능
    ans = max(ans, max(row))
print(ans-1)