"""
Pass - 33076KB 40ms

내장 함수
    - bin(숫자) : 숫자를 2진수로 표현한 뒤, prefix로 0b를 붙임
"""
import sys
sys.stdin = open("input.txt")

print(bin(int(input(), 8))[2:])