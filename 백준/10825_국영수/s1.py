"""
Pass - 50376KB 444ms
"""
import sys
sys.stdin = open('input.txt')

N = int(input())
scores = {}
for _ in range(N):
    name, k, e, m = sys.stdin.readline().split()
    if int(k) in scores:
        if int(e) in scores[int(k)]:
            if int(m) in scores[int(k)][int(e)]:
                scores[int(k)][int(e)][int(m)].append(name)
            else:
                scores[int(k)][int(e)][int(m)] = [name]
        else:
            scores[int(k)][int(e)] = {int(m): [name]}
    else:
        scores[int(k)] = {int(e): {int(m): [name]}}
for k in sorted(scores.keys(), reverse=True):
    for e in sorted(scores[k].keys()):
        for m in sorted(scores[k][e].keys(), reverse=True):
            for name in sorted(scores[k][e][m]):
                print(name)