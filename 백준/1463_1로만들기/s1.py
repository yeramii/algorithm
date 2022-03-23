'''
Pass
    Python3 - 메모리 30864 KB, 시간 932 ms
    PyPy3 - 메모리 128544 KB, 시간 300 ms

[내 풀이]: 재귀함수 + prunning
'''
import sys
sys.stdin = open('input.txt')

X = int(input())
minimum = 10 ** 6

def cnt_operation(n, cnt):
    global minimum

    if cnt >= minimum:
        return
    if n == 1:
        minimum = cnt
        return

    if n % 3 == 0:
        cnt_operation(n // 3, cnt + 1)
    if n % 2 == 0:
        cnt_operation(n // 2, cnt + 1)
    cnt_operation(n - 1, cnt + 1)

cnt_operation(X, 0)
print(minimum)