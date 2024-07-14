"""
Pass - DFS : 31120KB 44ms

내가 공식을 찾아서 막구현을 하다가 틀려서, DFS가 훨씬 효율적이라는 것을 알아버렸다..
s2) combintaion을 모두 구해서 각 배열을 검사 -> 시간 오래 소요 + 틀림
"""

import sys
sys.stdin = open("input.txt")

L, C = map(int, input().split())
lst = input().split()
lst.sort()
vowels = ['a', 'e', 'i', 'o', 'u']
visited = [0] * len(lst)

def check_vowels(lst):
    vnum = 0
    for c in lst:
        if c in vowels:
            vnum += 1
    cnum = len(lst) - vnum
    if vnum >= 1 and cnum >= 2:
        print(''.join(lst))
    return

def dfs(s, n, l):
    if n == L:
        check_vowels(l)
        return
    for i in range(s, len(lst)):
        if not visited[i]:
            l.append(lst[i])
            visited[i] = 1
            dfs(i+1, n+1, l)
            visited[i] = 0
            l.pop(-1)

dfs(0, 0, [])
