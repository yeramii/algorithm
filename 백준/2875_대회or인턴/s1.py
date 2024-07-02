import sys
sys.stdin = open("input.txt")

W, M, K = map(int, input().split())
team = min(W//2, M) # 1 team = 3 person
remains = W + M - team * 3
while team >= 0:
    if remains >= K:
        break
    else:
        team -= 1
        remains = W + M - team * 3
print(team)