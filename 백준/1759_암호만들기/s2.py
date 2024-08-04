from itertools import combinations

L, C = map(int, input().split())
vowels = []
consonants = []
for s in input().split():
    if s in ['a', 'e', 'i', 'o', 'u']:
        vowels.append(s)
    else:
        consonants.append(s)
tmp = []
needs = L - 3
extra_v = len(vowels) - 1
extra_c = len(consonants) - 1
if needs:
    max_v = min(needs, extra_v)
    max_c = min(needs, extra_c)
    for i in range(max_v, -1, -1):
        if needs - i > max_c: break
        tmp.append(i+1)
else:
    tmp.append(1)

for vnum in tmp:
    cnum = L - vnum
    for v in combinations(vowels, vnum):
        for c in combinations(consonants, cnum):
            tmp = list(v) + list(c)
            tmp.sort()
            print(''.join(tmp))