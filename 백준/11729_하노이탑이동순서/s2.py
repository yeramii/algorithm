"""
Fail
대실패.... 재귀가 안 끝남
"""
import sys
sys.stdin = open("input.txt")

N = int(input())
h = { 1: [i for i in range(N, 0, -1)], 2: [], 3: [] }
ans_cnt = 10 ** 6
ans_stack = []

def move_pan(i1, i2, cnt, stack):
    global h
    tmp = h[i1].pop()
    h[i2].append(tmp)
    stack.append((i1, i2))
    dfs(cnt + 1, stack, i2)
    h[i1].append(tmp)
    h[i2].pop()
    stack.pop()


def dfs(cnt, stack, last):
    global ans_cnt, ans_stack
    if cnt >= ans_cnt:
        return
    if len(h[3]) == N:
        ans_cnt = cnt
        ans_stack = stack
        return

    if h[1] and last != 1:
        if not h[2] or (h[2] and h[1][-1] < h[2][-1]):
            move_pan(1, 2, cnt, stack)
        if not h[3] or (h[3] and h[1][-1] < h[3][-1]):
            move_pan(1, 3, cnt, stack)
    if h[2] and last != 2:
        if not h[1] or (h[1] and h[2][-1] < h[1][-1]):
            move_pan(2, 1, cnt, stack)
        if not h[3] or (h[3] and h[2][-1] < h[3][-1]):
            move_pan(2, 3, cnt, stack)
    if h[3] and last != 3:
        if not h[1] or (h[1] and h[3][-1] < h[1][-1]):
            move_pan(3, 1, cnt, stack)
        if not h[2] or (h[2] and h[3][-1] < h[2][-1]):
            move_pan(3, 2, cnt, stack)

dfs(0, [], 0)
