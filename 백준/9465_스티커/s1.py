'''
Python3 - Pass

풀이 : DP (문제에서 주어진 수의 범위를 차례대로 진행해보며 규칙 찾기)

    - n=1 부터 차례대로 올라가며 max 찾기
    - n=1, n=2인 경우를 고려하지 않아서 계속 런타임 에러(IndexError) 발생함
'''

import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        print(max(mat[0][0], mat[1][0]))
    else:
        mat[0][1] += mat[1][0]
        mat[1][1] += mat[0][0]

        if n == 2:
            print(max(mat[0][1], mat[1][1]))
        else:
            for c in range(2, n):
                mat[0][c] += max(mat[1][c-1], mat[1][c-2])
                mat[1][c] += max(mat[0][c-1], mat[0][c-2])
            print(max(mat[0][n-1], mat[1][n-1]))
