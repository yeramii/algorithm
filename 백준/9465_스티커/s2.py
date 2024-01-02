'''
Python3 - Fail

풀이 : 처음 풀 때 원리는 이해했지만, dp로 max를 차례대로 구하는 것이 아닌 모든 경우의 max를 구해봄
'''
import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(2)]

    r, c = 0, 0
    tmp = mat[r][c]
    while c < n-1:
        if ((c < n-2) and (mat[r][c+2] + mat[(r+1)%2][c+1] > mat[(r+1)%2][c+2])) or (c == n-2):
            r = (r+1) % 2
            c += 1
            tmp += mat[r][c]
        else:
            r = (r+1) % 2
            c += 2
            tmp += mat[r][c]
    score_max = tmp

    r, c = 1, 0
    tmp = mat[r][c]
    while c < n-1:
        if ((c < n-2) and (mat[r][c+2] + mat[(r+1)%2][c+1] > mat[(r+1)%2][c+2])) or (c == n-2):
            r = (r+1) % 2
            c += 1
            tmp += mat[r][c]
        else:
            r = (r+1) % 2
            c += 2
            tmp += mat[r][c]
    if tmp > score_max: score_max = tmp
    print(score_max)