import sys
sys.stdin = open("input.txt")

N = int(input())
N_cards = list(map(int, input().split()))
M = int(input())
M_cards = list(map(int, input().split()))

d = dict()
for m in M_cards:
    d[m] = 0
for n in N_cards:
    d[n] = 1
for m in M_cards:
    print(d[m])