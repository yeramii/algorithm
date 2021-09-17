import sys
sys.stdin = open('input.txt')

M, N = map(int, input().split())
M, N = 1, 100

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
