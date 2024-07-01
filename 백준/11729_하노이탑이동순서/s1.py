"""
Pass - 31120KB 880ms
하노이의 탑 - 대표적인 재귀 문제

다른 사람의 풀이 참고..
"""
import sys
sys.stdin = open("input.txt")

def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return
    hanoi(n-1, start, 6-start-end)  # 1. 1~N-1 원판을 start -> 6-start-end로 이동
    print(start, end)               # 2. N 원판을 start -> end로 이동
    hanoi(n-1, 6-start-end, end)    # 3. 1~N-1개의 원판을 6-start-end -> end로 이동

N = int(input())
print(2 ** N - 1)
hanoi(N, 1, 3)
