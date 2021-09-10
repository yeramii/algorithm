import sys
sys.stdin = open('input.txt')


K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]

l = 1
h = max(lans)

while l <= h:
    m = (l + h) // 2

    part = 0
    for lan in lans:
        part += lan // m

    if part < N:
        h = m - 1
    else:
        result = m
        l = m + 1

print(result)