"""
유클리드 호제법
        : 두 양의 정수 a, b(a > b)에 대하여 a, b의 최대공약수는 b, r의 최대공약수와 같다.
            gcd(a, b) = gcd(b, r)
        r = 0이라면 a, b의 최대공약수는 b가 된다. (r = a % b)

        ex) gcd(6, 8)
            6 % 8 = 6
            8 % 6 = 2
            6 % 2 = 0
            -> 나머지의 값이 0일 때의 b값인 2가 최대공약수

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