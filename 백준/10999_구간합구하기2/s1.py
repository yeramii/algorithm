"""
Pass - 207700KB 1164ms

segment tree with lazy propagation
"""
# https://4legs-study.tistory.com/128
from math import ceil, log


def init_tree(start, end, node):
    """
    tree 초기화

    start~end: 포용하는 leaf 범위
    node: 현재 tree node
    """
    global tree

    if start == end:
        tree[node] = leaf[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init_tree(start, mid, node*2) + init_tree(mid+1, end, node*2+1)
    return tree[node]


def update_lazy(start, end, node):
    """
    현재 node에 lazy가 존재하면 tree에 반영하고, 자식 node에 물려줌

    start~end: 포용하는 leaf 범위
    node: 현재 tree node
    """
    global tree, lazy

    if not lazy[node]: return
    tree[node] += (end - start + 1) * lazy[node]
    if start != end:
        lazy[node*2] += lazy[node]
        lazy[node*2 + 1] += lazy[node]
    lazy[node] = 0


def update_tree(start, end, node, left, right, val):
    """
    현재 node에 lazy가 존재하면 tree에 반영하고 tree update
    현재 node에 val을 더할 때, 자식 node의 lazy에 val 추가

    start~end: 현재 node가 포용하는 leaf 범위
    node: 현재 tree node
    left~right: 변경할 타겟 leaf
    val: 이 값만큼 더함
    """
    global tree, lazy

    update_lazy(start, end, node)

    if start > right or end < left:
        return
    if left <= start and end <= right:
        tree[node] += (end-start+1) * val
        if start != end:
            lazy[node*2] += val
            lazy[node*2 + 1] += val
        return
    mid = (start + end) // 2
    update_tree(start, mid, node * 2, left, right, val)
    update_tree(mid + 1, end, node * 2 + 1, left, right, val)
    tree[node] = tree[node*2] + tree[node*2+1]
    return

def query_sum(start, end, node, left, right):
    """
    start~end: 현재 node가 포용하는 leaf 범위
    node: 현재 node
    left~right: 합을 구하는 leaf 범위
    """
    update_lazy(start, end, node)

    # 포함 X
    if start > right or end < left:
        return 0
    # 완전 포함
    if left <= start and end <= right:
        return tree[node]
    # 일부 포함
    mid = (start + end) // 2
    return query_sum(start, mid, node*2, left, right) + query_sum(mid+1, end, node*2+1, left, right)


N, M, K = map(int, input().split())
leaf = []
for _ in range(N):
    leaf.append(int(input()))

H = ceil(log(len(leaf), 2))
tree_size = pow(2, H+1) - 1
tree = [0] + [0] * tree_size
lazy = [0] + [0] * tree_size
init_tree(0, len(leaf)-1, 1)

for _ in range(M+K):
    tmp = list(map(int, input().split()))
    if tmp[0] == 1: # b~c까지 d를 더하기
        update_tree(0, len(leaf)-1, 1, tmp[1]-1, tmp[2]-1, tmp[3])
    else:           # b~c의 합을 출력
        print(query_sum(0, len(leaf)-1, 1, tmp[1]-1, tmp[2]-1))