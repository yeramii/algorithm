'''
Python3 - Fail (시간초과)
PyPy3 - Pass

풀이: 가장 높은 위치 ~ 가장 낮은 위치를 만들어보고, 최소 시간보다 적으면 시간과 결과 높이를 update
    -> 답은 맞지만 전부 다 구해서 연산량 초과인듯?
    -> 은 걍 PyPy3으로 하니까 Pass
'''

import sys
sys.stdin = open('input.txt')

N, M, B = map(int, input().split())
land = []

# 변수 설정 및 land 초기화
min_t = 500 * 500 * 256
max_h = 0
min_h = 256
sum_h = 0
ans = 0
for _ in range(N):
    tmp = list(map(int, input().split()))
    land.append(tmp)
    if max(tmp) > max_h:
        max_h = max(tmp)
    if min(tmp) < min_h:
        min_h = min(tmp)
    sum_h += sum(tmp)

# 본격 최소 시간과 그 때의 높이 찾기
height = max_h
while height >= min_h:
    # 높이 못 만들면 1 낮추고 재시도
    if sum_h + B < height * M * N:
        height -= 1
        continue

    # 높이 만들 수 있으면 채우자! (최소 시간 고려)
    tmp_t = 0
    for i in range(N):
        for j in range(M):
            tmp_h = land[i][j] - height
            if tmp_h > 0:
                tmp_t += 2 * tmp_h
            else:
                tmp_t -= tmp_h

            if tmp_t >= min_t:
                break

    # 높이 만들었으면 최소 시간과 비교
    if tmp_t < min_t:
        min_t = tmp_t
        ans = height

    height -= 1

print(min_t, ans)
