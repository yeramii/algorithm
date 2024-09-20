import sys
sys.stdin = open("input.txt")
from math import inf

def find_tetromino(r, c):
    global ans

    tmp = -inf
    if c + 2 < C:  # tmp1 for 1 over ...
        tmp1 = -inf
        if r - 1 >= 0:
            tmp1 = max(nums[r-1][c+1], nums[r-1][c+2])  # .:., ..:
            tmp = max(tmp, nums[r][c] + nums[r][c + 1] + nums[r - 1][c + 1] + nums[r - 1][c + 2]) # .:'
        if c + 3 < C:
            tmp1 = max(tmp1, nums[r][c+3])  # ....
        if r + 1 < R:
            tmp1 = max(tmp1, nums[r+1][c], nums[r+1][c+1], nums[r+1][c+2])  # :'', ':', '':
        if tmp1 != -inf:
            tmp = tmp1 + sum(nums[r][c:c+3])
    if c + 1 < C and r + 1 < R:  # tmp2 for 1 over ': / tmp3 for 1 over :.
        tmp2 = nums[r+1][c] # ::
        tmp3 = -inf
        if r - 1 >= 0:
            tmp2 = max(tmp2, nums[r-1][c+1])    # ㅓ
            tmp = max(tmp, nums[r][c] + nums[r+1][c] + nums[r][c+1] + nums[r-1][c+1])   # ┏┚
        if c + 2 < C:
            tmp2 = max(tmp2, nums[r+1][c+2])    # ':.
            tmp3 = max(tmp3, nums[r+1][c+2])    # :..
        if r + 2 < R:
            tmp2 = max(tmp2, nums[r+2][c+1])    # ┓
            tmp3 = max(nums[r+2][c], nums[r+2][c+1])    # ㅏ, ┗┓
        tmp = max(tmp, tmp2 + nums[r][c] + nums[r][c+1] + nums[r+1][c+1])
        if tmp3 != -inf:
            tmp = max(tmp, tmp3 + nums[r][c] + nums[r+1][c] + nums[r+1][c+1])
    if r+2 < R: # tmp4 for 1 over ㅣ
        tmp4 = -inf
        if r + 3 < R:
            tmp4 = nums[r+3][c] # ┃
        if c + 1 < C:
            tmp4 = max(tmp4, nums[r+2][c+1], nums[r][c+1])  # ┗, ┏
        if c - 1 >= 0:
            tmp4 = max(tmp4, nums[r+2][c-1])    # ┛
        if tmp4 != -inf:
            tmp = max(tmp, tmp4 + nums[r][c] + nums[r+1][c] + nums[r+2][c])
    if r-1 >= 0 and c+2 < C:
        tmp = max(tmp, nums[r][c] + nums[r][c+1] + nums[r-1][c+1] + nums[r-1][c+2]) # .:'
    if tmp > ans:
        ans = tmp

R, C = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(R)]
ans = -inf

for r in range(R):
    for c in range(C):
        find_tetromino(r, c)
print(ans)
