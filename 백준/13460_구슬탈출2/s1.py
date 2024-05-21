"""
Pass - 31120KB 236ms

BFS 안쓰고 그냥 풀었다 ..
"""
import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
table = []
for r in range(N):
    tmp = input()
    row = []
    for i, c in enumerate(tmp):
        if c == "R":
            R = [r, i]
            c = "."
        if c == "B":
            B = [r, i]
            c = "."
        row.append(c)
    table.append(row)
ans = 11

def tilt_table(cnt, R, B):
    """
    table을 기울이며, 지금까지 기울인 횟수를 반환한다.

    cnt: table 기울일 횟수
    R : R 좌표 [r, c]
    B : B 좌표 [r, c]
    """
    global ans
    # 10 초과째 기울일거면 반환
    if cnt >= ans:
        return

    # 상 하 좌 우
    for i in range(4):
        # 테이블을 i 방향으로 기울인다. (볼이 끝까지 움직일 때까지)
        [RR, BB] = move_balls(R, B, i)
        if [RR, BB] == [R, B]:
            continue
        if RR == [-1, -1] and BB != [-1, -1]:
            if cnt < ans:
                ans = cnt
            return
        elif BB == [-1, -1]:
            continue
        tilt_table(cnt+1, RR, BB)


def move_balls(R, B, direction):
    """
    table 위의 R, B 볼들을 한 방향으로 이동시킨다.
    """
    # 방향 (상 하 좌 우)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    # 방향에 따라 어떤 볼을 먼저 이동시킬지 결정
    firstball = "R"
    if (direction == 0 and R[0] > B[0]) or (direction == 1 and R[0] < B[0]) or (direction == 2 and R[1] > B[1]) or (direction == 3 and R[1] < B[1]):
        firstball = "B"
    if firstball == "R":
        RR = roll_a_ball(R, B, dr[direction], dc[direction])
        BB = roll_a_ball(B, RR, dr[direction], dc[direction])
    else:
        BB = roll_a_ball(B, R, dr[direction], dc[direction])
        RR = roll_a_ball(R, BB, dr[direction], dc[direction])
    return [RR, BB]


def roll_a_ball(target, other, dr, dc):
    """
    target ball을 dr, dc 방향으로 가능한 많이 이동시키고 위치를 반환한다.
    other ball의 위치 고려
    구멍에 빠졌을 경우 [-1, -1] 반환
    """
    # target 위치
    rr = target[0]
    cc = target[1]
    is_hole = False
    while True:
        rr += dr
        cc += dc
        if rr not in range(N) or cc not in range(M):
            break
        if table[rr][cc] == "#" or other == [rr, cc]:
            break
        if table[rr][cc] == "O":
            is_hole = True
            break
    if is_hole:
        return [-1, -1]
    else:
        return [rr-dr, cc-dc]

tilt_table(1, R, B)
if ans > 10:
    print(-1)
else:
    print(ans)