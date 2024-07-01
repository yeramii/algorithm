"""
Pass - 31120KB 48ms
"""
import sys
sys.stdin = open("input.txt")

N = int(input())
arr = [input() for _ in range(N)]

def dfs(r, c, n):
    start = arr[r][c]
    is_same = True
    for rr in range(r, r+n):
        for cc in range(c, c+n):
            if arr[rr][cc] != start:
                is_same = False
                break
    if is_same:
        return start
    else:
        a1 = dfs(r, c, n//2)
        a2 = dfs(r, c+n//2, n//2)
        a3 = dfs(r+n//2, c, n//2)
        a4 = dfs(r+n//2, c+n//2, n//2)
        return f"({a1}{a2}{a3}{a4})"

print(dfs(0, 0, N))