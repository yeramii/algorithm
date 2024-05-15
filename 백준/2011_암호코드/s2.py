"""
Fail - 시간 초과

DP 문제인데, 재귀 호출하느라 시간 초과된 듯
"""

import sys
sys.stdin = open('input.txt')

C = input()
cnt = 0

def count_crypto(cryp: str) -> None:
    """
    1. 길이가 1 이하이고 0이 아니면, cnt ++하고 return
    2. 길이가 2 이상이고 맨 앞이 0이 아니면,
        1) 맨 앞 자르고 뒤에 애들을 보냄
        2) 두 번째까지 잘랐을 때 26 이하인지 검사하여 맞으면 뒤에 애들을 보냄
    """

    global cnt

    if len(cryp) < 2:
        if cryp != '0':
            cnt += 1
    elif cryp[0] != '0':
        count_crypto(cryp[1:])
        if int(cryp[:2]) in range(1, 27):
            count_crypto(cryp[2:])

if C[0] == '0':
    print(0)
else:
    count_crypto(C)
    print(cnt)

