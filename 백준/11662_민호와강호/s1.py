"""
Pass
s1) 구글링 - 33240KB 40ms
s2) 내 풀이 - 31120KB 76ms

이분 탐색 vs 삼분 탐색
    - 이분 탐색 : 정렬된 수열 (단조 증가/감소)에서 원하는 값을 찾는 탐색 (1차 그래프)
    - 삼분 탐색 : 오목/볼록한 수열에서 극값을 찾는 탐색 (2차 그래프)

삼분 탐색 (Ternary Search)
    - U 혹은 Λ 모양의 그래프를 탐색 (오목/볼록한 지점이 1개)
    - 방법 (가정: 최소값을 찾는 U 모양의 그래프)
        1. 시작 구간 정의 [lo, hi] : 좌측 끝 (lo), 우측 끝 (hi)
        2. 구간을 3등분 : [lo, p], [p, q], [q, hi]
        3. 두 점 p, q의 함수값을 구했을 때,
            1) f(p) > f(q) 라면 [lo, p]에는 최소값이 존재 X (∵ lo->p->q가 감소)
                -> ∴ p를 lo로 설정
            2) f(p) < f(q) 라면 [q, hi]에는 최소값이 존재 X (∵ p->q->hi가 증가)
                -> ∴ q를 hi로 설정
            => 구간을 2/3로 줄여가며, 오차 범위까지 탐색 반복
    - 시행 횟수
        . 매 루프마다 문제의 크기가 2/3으로 줄어드므로, 원래 구간 크기가 N일 때 O(logN) 번의 시행 후 결과에 도달
    - 한계
        . 최솟값이 아닌데 평탄한 구간이 존재하는 경우, 삼분 탐색 사용 불가
            = 평탄한 구간이 최솟값이면 가능

소수점 지정 방법
    1) round(실수, 자릿수)
        = round(ans, 10)
    2) f-string
        = f"실수:.자릿수f"
        = f"{ans:.10f}"
    3) "{}".format()
        = "{:자릿수f}.format(실수)
        = "{:.10f}".format(ans)
    4) format(실수, ".자릿수f")
        = format(ans, ".10f")
"""

import sys
import math
sys.stdin = open("input.txt")

x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())    # 실수
def minho(dist):    # dist = 이동 거리 (0~100)
    return [x1 + (x2-x1) * (dist/100), y1 + (y2-y1) * (dist/100)]
def kangho(dist):
    return [x3 + (x4-x3) * (dist/100), y3 + (y4-y3) * (dist/100)]

ans = math.sqrt(pow(10000, 2) + pow(10000, 2))     # 문제 상 민호-강호 거리의 최대

# 이동 거리 비율 (%)
lo = 0
hi = 100
while (hi-lo >= 1e-7):  # 오차 범위 10^-6
    p = (2*lo + hi) / 3
    q = (lo + 2*hi) / 3
    mp = minho(p)
    mq = minho(q)
    kp = kangho(p)
    kq = kangho(q)
    dist_p = math.sqrt(pow(mp[0]-kp[0], 2) + pow(mp[1]-kp[1], 2))
    dist_q = math.sqrt(pow(mq[0]-kq[0], 2) + pow(mq[1]-kq[1], 2))
    ans = min(ans, min(dist_p, dist_q))
    if dist_p >= dist_q:
        lo = p
    else:
        hi = q

print(f"{ans:.10f}")