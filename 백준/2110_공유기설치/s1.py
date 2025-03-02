"""
Pass - 38848KB 524ms
: 다른 사람의 풀이 (이진 탐색)

(Point) 이진 탐색의 대상을 공유기 간의 거리로 설정 !!!
- s1.py 에선 모든 공유기 설치 조합에서 최대를 구했음

"""
import sys
sys.stdin = open("input.txt")

N, C = map(int, input().split())
houses = [int(sys.stdin.readline()) for _ in range(N)]
houses.sort()

# 공유기 간 거리의 최소/최대
start = 1
end = houses[-1] - houses[0]

while start <= end:
    mid = (start + end) // 2    # 공유기 사이의 최소 거리
    curr = houses[0]            # 공유기 위치
    cnt = 1
    for i in range(1, len(houses)):
        if houses[i] >= curr + mid:
            cnt += 1
            curr = houses[i]
    # 공유기 설치 수가 목표보다 많으면 공유기 간 거리 넓힘
    if cnt >= C:
        start = mid + 1
    # 공유기 설치 수가 목표보다 적으면 공유기 간 거리 좁힘
    else:
        end = mid - 1
print(end)