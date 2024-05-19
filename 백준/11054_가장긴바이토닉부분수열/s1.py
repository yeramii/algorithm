import sys
sys.stdin = open('input.txt')

N = int(input())
A = list(map(int, input().split()))
inc = [1] * N
dec = [1] * N
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            inc[i] = max(inc[i], inc[j]+1)
        if A[N-1-i] > A[N-1-j]:
            dec[N-1-i] = max(dec[N-1-i], dec[N-1-j]+1)

ans = [x + y for x, y in zip(inc, dec)]
print(max(ans)-1)