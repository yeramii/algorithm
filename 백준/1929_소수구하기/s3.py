import sys
sys.stdin = open('input.txt')

M, N = map(int, input().split())
prime = [True] * (N + 1)

for num in range(2, int(N**(1/2)) + 1):
    if prime[num]:
        for i in range(2 * num, N + 1, num):
            prime[i] = False

for idx in range(M, N + 1):
    if idx > 1 and prime[idx]:
        print(idx)

'''
[에라토스테네스의 체]
-> 연산량 N/sqrt(N) 만큼 줄일 수 있다.

N이 소수인지 확인하려면 sqrt(N) 까지만 확인하면 된다.

'''