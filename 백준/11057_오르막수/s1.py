'''
Python3 -> Pass

풀이 : 나열해서 규칙 찾기

(각 자릿 수)   0 1 2 3 4 5 6 7 8 9
1            1 1 1 1 1 1 1 1 1 1
2           10 9 8 7 6 5 4 3 2 1
            => 해당 index부터 끝 index 까지 sum
'''
import sys
sys.stdin = open('input.txt')

N = int(input())
cnt = [[0]*10 for _ in range(N)]
cnt[0] = [1] * 10
for i in range(1, N):
    for j in range(10):
        cnt[i][j] = sum(cnt[i-1][j:])

print(sum(cnt[N-1]) % 10007)