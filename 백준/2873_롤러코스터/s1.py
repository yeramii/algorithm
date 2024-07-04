"""
s1 - Pass : 69776KB 584ms
s2 - Fail : 시간 초과 (dfs 사용)
"""
import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt")

R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

if not R % 2 and not C % 2:
    # 안 갈 좌표 : tmp_r, tmp_c
    tmp_min = 1000
    tmp_r = -1
    tmp_c = -1
    for r in range(R):
        for c in range(C):
            if (r + c) % 2 and arr[r][c] < tmp_min:
                tmp_min = arr[r][c]
                tmp_r = r
                tmp_c = c
    # mid : 안 갈 좌표가 포함된 2개 행의 경로
    # be, af : 안 갈 좌표가 포함되지 않은 2개 행의 경로 중 mid 행의 전, 후
    be = "R"*(C-1) + "D" + "L"*(C-1)
    af = "L"*(C-1) + "D" + "R"*(C-1)
    if not tmp_r % 2:
        mid = "D" + "RURD"*(C//2-1)
        cidx = 4 * (tmp_c // 2)
        mid = mid[:cidx+1] + "R" + mid[cidx+1:]
    else:
        mid = "DRUR"*(C//2-1) + "D"
        cidx = 4 * (tmp_c // 2)
        mid = mid[:cidx] + "R" + mid[cidx:]
    ans = ""
    for i in range(R//2):
        if i < tmp_r//2:
            ans += be
        elif i == tmp_r//2:
            ans += mid
        else:
            ans += af
        if i != R//2-1:
            ans += "D"
    print(ans)
else:
    if R % 2:
        print("R"*(C-1) + ("D" + "L"*(C-1) + "D" + "R"*(C-1)) * (R//2))
    else:
        print("D"*(R-1) + ("R" + "U"*(R-1) + "R" + "D"*(R-1)) * (C//2))