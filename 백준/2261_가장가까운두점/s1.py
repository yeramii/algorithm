"""
나 - 완전 탐색 (Fail)
구글링 - 분할 정복 (Pass)

idea
    1. x 좌표를 기준으로 오름차순 정렬한 뒤, 가운데 점을 기준으로 배열을 분할한다.
    2. 2개 이상 남을 때까지 (2 or 3) 분할한 뒤, 그들끼리의 최소를 구한다.
"""

import sys
sys.stdin = open("input.txt")

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
points.sort()

def cal_minimum_dist(start, end):
    """ start~end 까지의 group 내에서 최소 거리 구하기 - 완전 탐색 """
    min_dist = 1e10
    for i in range(start, end-1):    # 0~n-2
        for j in range(i+1, end):   # i~n-1
            tmp = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
            if tmp < min_dist:
                min_dist = tmp
    return min_dist


def find_minimum_dist(start, end):
    """ start~end 까지의 group 내에서 최소 거리 구하기 - 분할 정복 """
    size = end - start
    if size < 3:
        return cal_minimum_dist(start, end)

    # 왼쪽 그룹과 오른쪽 그룹에서 각각 찾기
    mid = (start + end) // 2
    left = find_minimum_dist(start, mid)
    right = find_minimum_dist(mid, end)
    min_dist = min(left, right)

    # 가운데 그룹 범위 정의: (중간x - min_dist//2 <= x좌표 <= 중간x + min_dist//2)
    middle_group = []
    divide_x = points[mid][0]
    for i in range(start, end):
        if (points[i][0] - divide_x) ** 2 <= min_dist:
            middle_group.append(points[i])
    middle_group.sort(key=lambda x: x[1])

    # 가운데 그룹끼리의 거리 계산 (단, y좌표끼리의 차이가 min_dist보다 크면 계산 X)
    for i in range(len(middle_group)):
        now = middle_group[i]
        for j in range(i+1, len(middle_group)):
            compare = middle_group[j]
            if (compare[1] - now[1]) ** 2 >= min_dist:
                break
            dist = (compare[0] - now[0]) ** 2 + (compare[1] - now[1]) ** 2
            min_dist = min(min_dist, dist)

    return min_dist

print(find_minimum_dist(0, n))