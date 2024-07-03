"""
Fail - 메모리 초과
"""
import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt")

R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

def get_score(score, r, c, direc):
    global tmp_max, tmp_direc

    if r == R-1 and c == C-1:
        if score > tmp_max:
            tmp_max = score
            tmp_direc = direc
            return
    for k in range(4):
        rr = r + dr[k]
        cc = c + dc[k]
        if rr not in range(R) or cc not in range(C): continue
        if visited[rr][cc]: continue
        visited[rr][cc] = 1
        get_score(score+arr[rr][cc], rr, cc, direc+dk[k])
        visited[rr][cc] = 0

if not R % 2 and not C % 2:
    # 현재는 dfs. 최적화 필요 !! (메모리 초과 ㅠ)
    visited = [[0] * C for _ in range(R)]
    dk = ["D", "U", "R", "L"]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    tmp_max = 0
    tmp_direc = ""
    visited[0][0] = 1
    get_score(arr[0][0], 0, 0, "")
    print(tmp_direc)
else:
    if R % 2:
        print("R"*(C-1) + ("D" + "L"*(C-1) + "D" + "R"*(C-1)) * (R//2))
    else:
        print("D"*(R-1) + ("R" + "U"*(R-1) + "R" + "D"*(R-1)) * (C//2))
