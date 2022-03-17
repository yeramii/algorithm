'''
Python3 - Pass (864ms)

풀이:
    1) 나무의 높이를 내림차순 정렬
    2) 몇 번째 나무까지 자를건지 찾고,
    3) 해당 나무에서 몇 번 더 잘라야할 지 계산
    -> s1보다 연산량을 줄인 풀이
'''

import sys
sys.stdin = open('input2.txt')

N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort(reverse=True)

sum_cut = [0]   # 해당 index 나무의 높이까지 잘랐을 때(해당 나무는 안 잘리게), 앞의 나무들이 잘린 총 높이
order = 1       # 현재 몇 index 의 나무까지 자르려 하는지

# 몇 번째 나무(order)까지 자를건지 결정
while order < N:
    tmp = sum_cut[-1] + (trees[order-1] - trees[order]) * order
    sum_cut.append(tmp)
    if tmp > M:
        break
    order += 1

# 현재 자르는 마지막 나무 원래 높이 - (더 필요한 높이 / 자르고 있는 나무 수)의 몫
height = trees[order-1] - (M-sum_cut[order-1]) // order
# (더 필요한 높이 / 자르고 있는 나무 수)의 나머지가 존재하면 한 번 더 자름
if (M-sum_cut[order-1]) % order:
    height -= 1

print(height)