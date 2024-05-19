"""
Python3 - Fail

풀이 : 제곱근부터 1씩 감소하며 빼는 방식
        -> TC 문제만 통과하고, 예외 case가 반영되지 않음
"""
import sys
sys.stdin = open('input.txt')

N = int(input())
start = (N ** 0.5) // 1
cnt = 0
while N:
    while N < start ** 2:
        start -= 1
    N -= start ** 2
    cnt += 1
print(cnt)
