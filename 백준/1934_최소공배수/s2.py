"""
Fail - 시간 초과

    단순 구현

"""
import sys
sys.stdin = open("input.txt")

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

for _ in range(int(input())):
    A, B = map(int, input().split())
    a = find_y(A)
    b = find_y(B)
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
