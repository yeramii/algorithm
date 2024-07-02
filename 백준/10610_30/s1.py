import sys
sys.stdin = open("input.txt")

N = input()
tmp = 0
for n in N:
    tmp += int(n)
if tmp % 3 or "0" not in N:
    print(-1)
else:
    lst = [n for n in N]
    lst.sort(reverse=True)
    print(''.join(lst))