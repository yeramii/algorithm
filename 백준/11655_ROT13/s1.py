"""
Pass - 31120KB 44ms
"""
import sys
sys.stdin = open("input.txt")

# a(97) z(122) A(65) Z(90)
for s in input():
    tmp = ord(s)
    if tmp in range(97, 123):
        ss = tmp + 13
        if ss > 122:
            ss -= 26
    elif tmp in range(65, 91):
        ss = tmp + 13
        if ss > 90:
            ss -= 26
    else:
        ss = tmp
    print(chr(ss), end='')

