import sys
sys.stdin = open('input.txt')

n = int(input())
sequence = [int(input()) for _ in range(n)]

stack = [1]
answer = ['+']
top = 1
num = 1
idx = 0
while num <= n:
    if not top or sequence[idx] != stack[top - 1]:
        num += 1
        if num > n:
            break
        stack.append(num)
        top += 1
        answer.append('+')
    else:
        answer.append('-')
        stack.pop(-1)
        idx += 1
        if idx == n:
            break
        top -= 1
        if top < 0:
            break

if idx != n or num != n:
    print('NO')
else:
    for ans in answer:
        print(ans)