"""
Pass - 31120KB 36ms
    괜히 머리 써서 각 공약수 저장하는 배열의 최대 크기를 sqrt(A) 만큼으로 했다가, 반례 (2, 2), (2, 4) 생각 못해서 틀렸었음

    출제 의도는 유클리드 호제법 사용!! -> s2.py
"""
import sys
sys.stdin = open("input.txt")
A, B = map(int, input().split())
def find_y(num):
    ans = [0] * (num+1)
    ans[1] = 1
    for i in range(2, num + 1):
        while num != 1:
            if num % i == 0:
                ans[i] += 1
                num //= i
            else:
                break
    if num != 1:
        ans[0] += 1
    return ans
a = find_y(A)
b = find_y(B)

ans = 1
for i in range(1, min(len(a), len(b))):
    if a[i] and b[i]:
        ans *= i ** min(a[i], b[i])
print(ans)

ans = 1
ab = [0] * max(len(a), len(b))
for i in range(2, len(a)):
    if a[i]:
        ab[i] = a[i]
for i in range(2, len(b)):
    if b[i] and b[i] > ab[i]:
        ab[i] = b[i]
for i in range(1, len(ab)):
    if ab[i]:
        ans *= i ** ab[i]
print(ans)