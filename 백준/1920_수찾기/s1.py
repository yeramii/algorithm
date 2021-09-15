import sys
sys.stdin = open('input.txt')

N = int(input())
lst_N = list(map(int, input().split()))

M = int(input())
lst_M = list(map(int, input().split()))

for m in lst_M:
    if m in lst_N:
        idx = lst_N.index(m)
        lst_N.pop(idx)
        print(1)
    else:
        print(0)

