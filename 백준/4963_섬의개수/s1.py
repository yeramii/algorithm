"""
Pass
s1 - DFS : 31500KB 88ms
s2 - BFS : 34072KB 100ms
"""
import sys
sys.stdin = open("input.txt")
sys.setrecursionlimit(10 ** 6)

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

def find_land(r, c, curr):
    if arr[r][c] != 1: return
    arr[r][c] = curr
    for i in range(8):
        rr = r + dr[i]
        cc = c + dc[i]
        if rr in range(h) and cc in range(w):
            find_land(rr, cc, curr)

while True:
    w, h = map(int, sys.stdin.readline().split())
    if not w and not h: break
    arr = []
    for _ in range(h):
        arr.append(list(map(int, sys.stdin.readline().split())))
    curr = 1
    for r in range(h):
        for c in range(w):
            if arr[r][c] != 1: continue
            curr += 1
            find_land(r, c, curr)
    print(curr-1)
