'''
Python3 - Fail (시간 초과)

풀이 : 재귀적 구조로 모든 가능한 숫자를 만들며 개수를 세었다.
'''

import sys
sys.stdin = open('input.txt')

N = int(input())
cnt = 0
def count_func(last, length):
    global cnt
    if length == N:
        cnt += 1
        return
    if last == 9:
        count_func(9, length+1)
    elif last == 0:
        count_func(1, length+1)
    else:
        count_func(last+1, length+1)
        count_func(last-1, length+1)

for i in range(1, 10):
    count_func(i, 1)

print(cnt % 10 ** 9)