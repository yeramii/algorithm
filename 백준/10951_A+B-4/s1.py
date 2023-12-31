'''
EOFError 예외처리하는 것보다, readlines() 으로 한번에 읽어 오는 것이 빠르다.

    - s1 : 메모리 31120KB, 시간 52ms
    - s2 : 메모리 31120KB, 시간 40ms
'''

import sys
sys.stdin = open('input.txt')  # IDLE로 파일 읽을 때 (제출할 때는 삭제)

# s1
lines = sys.stdin.readlines()
for line in lines:
    A, B = map(int, line.split())
    print(A+B)

# s2
while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except EOFError:
        break