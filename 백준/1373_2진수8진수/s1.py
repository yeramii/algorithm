"""
Pass
1. 직접 구현 - 59392KB 572ms
2. 내장 함수 - 33076KB 52ms
    - int(string, base=10) : string을 base 진수의 숫자로 만들어줌
    - oct(int) : int 숫자를 8진수로 변환 후 prefix "0o" 붙임
"""
import sys
sys.stdin = open("input.txt")

# 1. 직접 구현
bi = input()
tmp = []
s = 0
for i, c in enumerate(bi[::-1]):
    s += int(c) * (2 ** (i % 3))
    if i % 3 == 2 or i == len(bi)-1:
        tmp.append(str(s))
        s = 0
print("".join(tmp[::-1]))

# 2. 내장 함수 사용 - int, oct
print(oct(int(input(), 2))[2:])     # 0o314
