"""
Pass
dfs       - 38008KB 4440ms
+ pruning - 39028KB 312ms

알고리즘을 쓰는데 한계가 있어서 막구현과 dfs알고리즘을 섞어 씀
+ mas

s2) dfs로는 커버못하는 case 때문에 막구현으로 했다가 12%에서 실패
    -> if 문 많이 쓰다가 실수 나온듯. but 찾기 힘듬 ㅠ
s1) dfs와 막구현 case를 나눔
    -> dfs로 안되는 4가지 case만 막구현
        + max value 이용하여 pruning(가지치기)
"""
import sys
sys.stdin = open("input.txt")

def find_dfs(r, c, cnt, acc, visited):
    global ans

    if cnt == 4:
        if acc > ans:
            ans = acc
        return
    for k in range(3):
        rr = r + dr[k]
        cc = c + dc[k]
        if rr not in range(R) or cc not in range(C):
            continue
        if visited[rr][cc]:
            continue
        visited[rr][cc] = 1
        find_dfs(rr, cc, cnt+1, acc+nums[rr][cc], visited)
        visited[rr][cc] = 0

def find_oh(r, c):
    global ans

    if r+2 < R: # ㅏ ㅓ
        tmp = nums[r][c] + nums[r+1][c] + nums[r+2][c]
        if c+1 < C and tmp+nums[r+1][c+1] > ans:
            ans = tmp+nums[r+1][c+1]
        if c-1 >= 0 and tmp+nums[r+1][c-1] > ans:
            ans = tmp+nums[r+1][c-1]
    if c+2 < C: # ㅜ ㅗ
        tmp = nums[r][c] + nums[r][c+1] + nums[r][c+2]
        if r+1 < R and tmp+nums[r+1][c+1] > ans:
            ans = tmp+nums[r+1][c+1]
        if r-1 >= 0 and tmp+nums[r-1][c+1] > ans:
            ans = tmp+nums[r-1][c+1]

for _ in range(int(input())):
    R, C = map(int, input().split())
    nums = [list(map(int, input().split())) for _ in range(R)]
    ans = -1e8
    dr = [1, 0, 0]
    dc = [0, 1, -1]
    visited = [[0]*C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            visited[r][c] = 1
            find_dfs(r, c, 1, nums[r][c], visited)
            visited[r][c] = 0
            find_oh(r, c)
    print(ans)