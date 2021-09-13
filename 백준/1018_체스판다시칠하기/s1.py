import sys
sys.stdin = open('input2.txt')


N, M = map(int, input().split())
board = [input() for _ in range(N)]
min_block = 64

temp = []
for r in range(N - 7):
    for c in range(M - 7):
        start = board[r][c]
        cnt1 = 0
        cnt2 = 0

        for i in range(8):
            for j in range(8):
                if not (i + j) % 2:
                    if board[r + i][c + j] != start:
                        cnt1 += 1
                    else:
                        cnt2 += 1
                else:
                    if board[r + i][c + j] == start:
                        cnt1 += 1
                    else:
                        cnt2 += 1

        if cnt1 <= min_block:
            min_block = cnt1
        if cnt2 <= min_block:
            min_block = cnt2

print(min_block)
