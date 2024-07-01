"""
Pass - 69452KB 6720ms
"""
import sys
sys.stdin = open("input.txt")

N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = {-1: 0, 0: 0, 1: 0}

def split_paper(r, c, n):
    nn = n // 3
    for rr in range(r, r+n, nn):
        for cc in range(c, c+n, nn):
            judge_paper(rr, cc, nn)

def judge_paper(r, c, n):
    global ans
    tmp = arr[r][c]
    is_done = True
    for rr in range(r, r+n):
       for cc in range(c, c+n):
           if arr[rr][cc] != tmp:
               is_done = False
    if is_done:
        ans[tmp] += 1
    else:
        split_paper(r, c, n)

judge_paper(0, 0, N)
print(ans[-1], ans[0], ans[1], sep='\n')