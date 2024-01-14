'''
Python3 - Fail(IndexError)

풀이 : 주어진 배열을 거꾸로 놓고, 이전 칸을 밟은 경우와 밟지 않은 경우의 최댓값을 각각 first, second에 저장
'''
import sys
sys.stdin = open('input.txt')

N = int(input())
scores = [int(input()) for _ in range(N)]
scores = scores[::-1]
first = [0] * N     # 이전 칸을 밟지 않았을 때 최댓값
second = [0] * N    # 이전 칸을 밟았을 때 최댓값
second[1] = scores[1]
if N < 3:
    print(sum(scores))
else:
    for i in range(2, N):
        first[i] = max(first[i-2], second[i-2]) + scores[i]
        second[i] = first[i-1] + scores[i]
    print(scores[0] + max(first[N-1], second[N-1], second[N-2]))