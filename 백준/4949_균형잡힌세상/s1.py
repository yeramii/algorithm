'''
Python3 - Pass

s2의 오류 고친 풀이
'''
import sys
sys.stdin = open('input.txt')

match = {'(': ')', '[': ']'}
while True:
    is_balanced = True
    line = input()
    stack = []
    if line == '.':
        break

    for char in line:
        if char == '.':
            break

        if char in ['(', '[']:
            stack.append(char)

        elif char in [')', ']']:
            if stack:
                tmp = stack.pop()
            else:
                is_balanced = False
                break
            if match[tmp] != char:
                is_balanced = False
                break

    if is_balanced and not stack:
        print('yes')
    else:
        print('no')