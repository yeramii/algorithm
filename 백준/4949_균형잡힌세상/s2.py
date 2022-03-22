'''
Python3 - Fail

[문제 잘못 이해해서 생긴 오류]
1. 입력이 무한대로 들어오는 것이 아니라 맨 마지막 입력은 '.'만 들어온다.
    -> 알기 전: 입력의 개수를 모를 때 쓰는 방법인

        lines = sys.stdin.readlines()
        for line in lines:
            ...

        를 이용해서 풀었다.
    -> 문제 의도: 맨 마지막 입력이 들어오면 결과 문자열 출력하지 않고 끝나도록 함.

2. "짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다." 라는 조건에서,
    괄호 옆의 공백문자의 개수도 같은 걸로 착각
    ex) [ python] -> no, [ python ] -> yes
    -> 예제 입력과 예제 출력을 잘 비교해 봤더라면 생기지 않았을 일....
    -> 결론: 문제를 잘 읽자 ^^!

아래 풀이는 위의 오류를 모른 채 풀었던 풀이
'''


import sys
sys.stdin = open('input.txt')

lines = sys.stdin.readlines()
match = {'(': ')', '[': ']'}
for line in lines:
    stack = [''] * 100
    top = -1
    idx = 0
    ans = 'yes'

    while idx < len(line):
        char = line[idx]
        if char not in ['(', ')', '[', ']', '.']:
            idx += 1
            continue
        blank = 0
        index = idx
        # 왼쪽 괄호가 나오면,
        if char in ['(', '[']:
            # 뒤에 붙은 공백의 갯수를 세서 함께 stack 에 쌓는다.
            while index < len(line):
                index += 1
                if line[index] == ' ':
                    blank += 1
                    continue
                else:
                    break
            top += 1
            stack[top] = char + str(blank)
            idx += (blank + 1)

        # 오른쪽 괄호가 나오면,
        elif char in [')', ']']:
            # 왼쪽 괄호 있으면 가져오고,
            if top < 0:
                ans = 'no'
                break
            left = stack[top]
            top -= 1
            # 괄호 짝 맞는지 확인 후, 공백 개수 확인
            if match[left[0]] != char:
                ans = 'no'
                break
            while index > 0:
                index -= 1
                if line[index] == ' ':
                    blank += 1
                    continue
                else:
                    break
            if str(blank) != left[1]:
                ans = 'no'
                break
            idx += 1

        # 온점 나왔으면, stack에 남은게 있는지 확인
        elif char == '.':
            if top > 0:
                ans = 'no'
            break

    print(ans)