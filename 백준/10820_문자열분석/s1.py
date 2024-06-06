"""
Pass
    1) input()으로 한 줄씩 받기 - 31120KB 56ms
    2) readlines()으로 한 번에 받기 (s2.py) - 31120KB 48ms
"""
import sys
sys.stdin = open("input.txt")

while True:
    try:
        n = input()
        # 소문자 97~122 / 대문자 65~90 / 숫자 48~57 / 공백 32( ), 9(\t), 10(\n)
        ans = [0, 0, 0, 0]
        for s in n:
            tmp = ord(s)
            if tmp in range(97, 123):
                ans[0] += 1
            elif tmp in range(65, 91):
                ans[1] += 1
            elif tmp in range(48, 58):
                ans[2] += 1
            elif tmp != 10:
                ans[3] += 1
        print(' '.join(map(str, ans)))
    except EOFError as e:
        break