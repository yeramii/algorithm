'''
Python3 -> Pass

풀이 : 경우의 수를 나열하여 패턴 찾기

(각 자릿 수)  0 1 2 3 4 5 6 7 8 9
1           0 1 1 1 1 1 1 1 1 1
10          1 1 2 2 2 2 2 2 2 1
100         1 3 3 4 4 4 4 4 3 2
            => 각 자리에서, "왼쪽 대각" + "오른 대각"
'''

import sys
sys.stdin = open('input.txt')

N = int(input())
cnt = [[0] * 10 for _ in range(N)]
cnt[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(1, N):
    for j in range(10):
        if j == 0:
            cnt[i][j] = cnt[i-1][j+1]
        elif j == 9:
            cnt[i][j] = cnt[i-1][j-1]
        else:
            cnt[i][j] = cnt[i-1][j+1] + cnt[i-1][j-1]

print(sum(cnt[N-1]) % 10 ** 9)