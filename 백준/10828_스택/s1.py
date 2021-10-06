'''
 아래 코드를 사용하는게 더 빠르다. (import sys도 제출 코드에 포함)
    import sys
    sys.stdin.readline()

 - Python3 => 29200 KB, 80 ms
 - PyPy3 => 127576 KB, 172 ms

'''

import sys

sys.stdin = open('input.txt')
N = int(sys.stdin.readline())

stack = [0] * N
top = -1
for _ in range(N):
    lst = sys.stdin.readline().split()

    if lst[0] == 'push':
        top += 1
        stack[top] = int(lst[1])
    elif lst[0] == 'pop':
        if top == -1:
            print(-1)
        else:
            print(stack[top])
            top -= 1
    elif lst[0] == 'size':
        print(top+1)
    elif lst[0] == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)
    elif lst[0] == 'top':
        if top == -1:
            print(-1)
        else:
            print(stack[top])