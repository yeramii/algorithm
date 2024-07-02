import sys
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)
ans = 0
for coin in coins:
    tmp = K // coin
    ans += tmp
    K -= tmp * coin
    if not K:
        break
print(ans)