'''
Python3 -> Pass

풀이 : 경우의 수 나열한 후, 배열 기반으로 변경하여 규칙 찾기
'''
import sys
sys.stdin = open('input.txt')

N = int(input())
cnt = [[0, 0] for _ in range(N)]
cnt[0] = [0, 1]
for r in range(1, N):
    cnt[r][0] = cnt[r-1][0] + cnt[r-1][1]
    cnt[r][1] = cnt[r-1][0]
print(sum(cnt[N-1]))