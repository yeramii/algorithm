"""
Pass - 37676KB 204ms

한 번 틀림 -> age를 문자열 형태로 저장한 뒤 정렬 -> 숫자 형태로 정렬하는 것과 다름
    ex) sorted(['1', '2', '3', '11', '22', '33']) = ['1', '11', '2', '22', '3', '33']
"""
import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
data = {}
for _ in range(N):
    age, name = sys.stdin.readline().split()
    if int(age) in data:
        data[int(age)].append(name)
    else:
        data[int(age)] = [name]
for a in sorted(data.keys()):
    for n in data[a]:
        print(a, n)