"""
1) array + sum() - Fail (시간 초과)
    - O(N)
    - 앞에서부터 하나씩 더해가므로 데이터의 개수만큼의 시간복잡도
2) segment tree - Pass (143936KB 1300ms)
    - O(logN)
    - 트리 구조의 특성 상 합을 구할 때 시간 복잡도 O(logN)
"""

import sys
sys.stdin = open("input.txt")

N, M, K = map(int, sys.stdin.readline().split())
leaf = [int(sys.stdin.readline()) for _ in range(N)]

### 1) array - 시간 초과  :O(N)
# for _ in range(M+K):
#     a, b, c = map(int, input().split())
#     if a == 1:
#         num[b-1] = c
#     elif a == 2:
#         print(sum(num[b-1:c]))


### 2) segment tree
# segment_tree[1] = 모든 노드의 합
# segment_tree[2] = 0~n//2번 노드의 합
# segment_tree[3] = n//2+1~n번 노드의 합
segment_tree = [0 for _ in range(4*N)]  # 포화이진트리 길이로 만들면 되지만, 주로 데이터 갯수*4

# 1. segment tree 만들기 : segment_tree[idx] 값 구하기
def init_tree(idx, start, end):
    """
    :param idx: 현재 tree node (1로 시작)
    :param start: 커버하는 leaf node의 시작 (0으로 시작)
    :param end: 커버하는 leaf node의 끝 (N-1로 시작)
    :return: 현재 tree node의 값
    """
    if start == end:
        segment_tree[idx] = leaf[start]
        return segment_tree[idx]
    mid = (start + end) // 2
    segment_tree[idx] = init_tree(idx*2, start, mid) + init_tree(idx*2+1, mid+1, end)
    return segment_tree[idx]


# 2. 구간 합 구하기
def find_tree(idx, start, end, left, right):
    """
    :param idx: 현재 tree node
    :param start: 현재 node가 커버하는 leaf의 시작
    :param end: 현재 node가 커버하는 leaf의 끝
    :param left: 탐색 leaf node의 시작
    :param right: 탐색 leaf node의 끝
    :return: 현재 tree node가 구간에 속하면 node의 값, 아니면 0
    """
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return segment_tree[idx]
    mid = (start + end) // 2
    return find_tree(idx*2, start, mid, left, right) + find_tree(idx*2+1, mid+1, end, left, right)


# 3. 값 변경 및 업데이트
def update_tree(idx, start, end, target, val):
    """
    :param idx: 현재 tree node
    :param start: 현재 node가 커버하는 leaf의 시작
    :param end: 현재 node가 커버하는 leaf의 끝
    :param target: 바꾸고자 하는 leaf의 번호
    :param val: 바꾸고자 하는 leaf의 차분 (변경값 - 현재값)
    :return:
    """
    if target < start or end < target:
        return
    segment_tree[idx] += val
    if start == end:
        return

    mid = (start + end) // 2
    update_tree(idx*2, start, mid, target, val)     # 왼쪽 자식 업데이트
    update_tree(idx*2+1, mid+1, end, target, val)   # 오른쪽 자식 업데이트

init_tree(1, 0, N-1)
for _ in range(M+K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        update_tree(1, 0, N-1, b-1, c-leaf[b-1])
        leaf[b-1] = c
    else:
        print(find_tree(1, 0, N-1, b-1, c-1))

