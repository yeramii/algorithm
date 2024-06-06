"""
유클리드 호제법
    - 최대공약수 (Greatest Common Divisor) : a & b의 최대 공약수는 b & a를 b로 나눈 나머지의 최대 공약수
        . from math import gcd
    - 최소공배수 (Least Common Multiple) : a와 b의 곱을 a와 b의 최대 공약수로 나눈 값
        . from math import lcm
"""
import sys
sys.stdin = open("input.txt")
a, b = map(int, input().split())

# 최대공약수 (Greatest Common Divisor)
# a & b의 최대 공약수는 b & a를 b로 나눈 나머지의 최대 공약수
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 최소공배수 (Least Common Multiple)
# a와 b의 곱을 a와 b의 최대 공약수로 나눈 값
def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))