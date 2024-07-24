import sys
sys.stdin = open("input.txt")

def check_3way(r, c, num):
    if num in arr[r]:
        return False
    for i in range(9):
        if arr[i][c] == num:
            return False
    for rr in range(3):
        for cc in range(3):
            if arr[3*(r//3)+rr][3*(c//3)+cc] == num:
                return False
    return True

def dfs(idx):
    global arr
    if idx == len(empty):
        for r in range(9):
            print(*arr[r])  # unpacking
        exit()
    (r, c) = empty[idx]
    for n in range(1, 10):
        if check_3way(r, c, n):
            arr[r][c] = n
            dfs(idx+1)
            arr[r][c] = 0

arr = []
empty = []
for r in range(9):
    tmp = list(map(int, input().split()))
    for c in range(9):
        if tmp[c] == 0:
            empty.append((r, c))
    arr.append(tmp)
dfs(0)