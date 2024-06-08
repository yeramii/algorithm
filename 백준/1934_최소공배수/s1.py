"""
Pass - 31120KB 128ms

유클리드 호제법
    : 두 양의 정수 a, b(a > b)에 대하여 a, b의 최대공약수는 b, r의 최대공약수와 같다.
        gcd(a, b) = gcd(b, r)
    r = 0이라면 a, b의 최대공약수는 b가 된다. (r = a % b)

    ex) gcd(6, 8)
        6 % 8 = 6
        8 % 6 = 2
        6 % 2 = 0
        -> 나머지의 값이 0일 때의 b값인 2가 최대공약수

"""
import sys
sys.stdin = open("input.txt")

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return int(a * b / gcd(a, b))

for _ in range(int(input())):
    A, B = map(int, input().split())
    print(lcm(A, B))