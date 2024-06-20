"""
Pass
s1 (이진 탐색) - 113088KB 3332ms
s2 (딕셔너리) - 143028KB 904ms
"""
import sys
sys.stdin = open("input.txt")

N = int(input())
N_cards = sorted(list(map(int, input().split())))
M = int(input())
M_cards = list(map(int, input().split()))

for m in M_cards:
    start = 0
    end = N-1
    while start <= end:
        mid = (start + end) // 2
        if N_cards[mid] <= m:
            start = mid + 1
        else:
            end = mid - 1
    if N_cards[end] == m:
        print(1)
    else:
        print(0)
