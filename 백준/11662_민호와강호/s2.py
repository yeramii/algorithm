"""
Pass - 31120KB 76ms

이분 탐색으로 실패해서 삼분 탐색 공부 후 while 문만 바꿔서 성공 ^0^
"""
import sys
sys.stdin = open("input.txt")

def calc_dist(M, N):
    return ((M[0] - N[0]) ** 2 + (M[1] - N[1]) ** 2) ** 0.5

Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = map(float, input().split())
ans = calc_dist((Ax, Ay), (Cx, Cy))
distA = calc_dist((Ax, Ay), (Bx, By))
distC = calc_dist((Cx, Cy), (Dx, Dy))

def moved(goneA):
    # gone : A가 간 거리 -> C가 간 거리 = gone * distC / distA
    AAx = Ax + goneA / distA * (Bx - Ax)
    AAy = Ay + goneA / distA * (By - Ay)
    CCx = Cx + goneA / distA * (Dx - Cx)
    CCy = Cy + goneA / distA * (Dy - Cy)
    return ((AAx, AAy), (CCx, CCy)) # 이동 후의 A, C 좌표

# goneA
lo = 0
hi = distA
while hi-lo >= 1e-7:    # 오차는 10^-6까지 허용
    p = (2*lo + hi) / 3
    q = (lo + 2*hi) / 3

    (moved_p1, moved_p2) = moved(p)
    (moved_q1, moved_q2) = moved(q)

    dist_p = calc_dist(moved_p1, moved_p2)
    dist_q = calc_dist(moved_q1, moved_q2)
    ans = min(ans, min(dist_p, dist_q))
    if dist_p >= dist_q:
        lo = p
    else:
        hi = q

print(round(ans, 10))
