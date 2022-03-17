'''
Python3 - Fail

풀이: 위에서부터 길이 1씩 자르며 필요한 높이 채웠는지 확인하는 방식
    -> 답은 맞지만 틀렸다. 너무 오래걸려서인 듯
        (N과 M의 범위가 엄청 큰 수였음)
    -> 이런 단순하고 있는 그대로의 풀이가 아니라, 빠른 방법이 필요
'''

import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort(reverse=True)

lack = [0] * N  # 최대 높이에서 부족한 높이
order = 0       # 몇 번째 index 의 나무까지 자르는 중인지
cut = 0         # 지금까지 몇 번 잘랐는지
for idx in range(N):
    tmp = trees[0] - trees[idx]
    lack[idx] = tmp
    if not tmp:
        order = idx

while M > 0:
    cut += 1            # 자른 횟수 증가!
    # 다음 나무도 잘리는지 확인하고, 나무 인덱스(cut) 업데이트
    if cut > lack[order + 1]:
        order += 1
    M -= (order + 1)    # 필요한 길이 -= 방금 자른 길이

print(trees[0] - cut)
