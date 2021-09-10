import sys
sys.stdin = open("input.txt")

x, y, w, h = map(int, input().split())
result = x
lst = [y, w-x, h-y]

for num in lst:
    if num < result:
        result = num

print(result)