import sys
sys.stdin = open('input.txt')

M, N = map(int, input().split())

if M < 3:
    print(2)
    M = 3

# 4 이상 짝
if not M % 2:
    for num in range(M + 1, N + 1, 2):
        temp = 0
        for i in range(3, num, 2):
            if not num % i:
                temp += 1
                break
        if not temp:
            print(num)

# 3 이상 홀
else:
    for num in range(M, N + 1, 2):
        temp = 0
        for i in range(3, num, 2):
            if not num % i:
                temp += 1
                break
        if not temp:
            print(num)

'''
[2씩 증가하며 검사]
-> 연산량 1/2 만큼 줄일 수 있다.

시작하는 수(M)가 홀수/짝수인 경우로 나눠, 마지막 수(N)까지 홀수만 세며 소수인지 검사

'''