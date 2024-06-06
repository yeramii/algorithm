"""
Pass - 37440KB 324ms
    cursor 기준으로 리스트를 나눔. (cursor의 위치를 기억하는게 아님)
"""
import sys
sys.stdin = open("input.txt")

s1 = list(sys.stdin.readline().rstrip())
s2 = [] # 커서 오른쪽 (뒤집힘)
for _ in range(int(sys.stdin.readline())):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == "L":
        if s1:
            s2.append(s1.pop())
    elif cmd[0] == "D":
        if s2:
            s1.append(s2.pop())
    elif cmd[0] == "B":
        if s1:
            s1.pop()
    elif cmd[0] == "P":
        s1.append(cmd[1])
s1.extend(reversed(s2))
print(''.join(s1))
