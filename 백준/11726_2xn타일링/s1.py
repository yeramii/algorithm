'''
Python3 - Pass

풀이: DP -> 점화식을 만들었다.
'''

import sys
sys.stdin = open('input.txt')

n = int(input())
rect = [0, 1, 2]
if n > 2:
    rect += [0] * (n-2)
    for i in range(3, n+1):
        rect[i] = rect[i-1] + rect[i-2]
print(rect[n] % 10007)