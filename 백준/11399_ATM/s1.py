import sys
sys.stdin = open("input.txt")

N = int(input())
P = list(map(int, input().split()))
P.sort(reverse=True)
ans = 0
for idx in range(len(P)):
    ans += P[idx] * (idx+1)
print(ans)