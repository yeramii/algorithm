"""
Pass - 31120KB 40ms

unicode <-> ascii
    - ord() : unicode를 입력 받아 ascii 값을 리턴
        ex) ord("a") = 97, ord("z") = 122
    - chr() : ascii 값을 입력 받아 unicode로 리턴
        ex) chr(97) = "a", chr(122) = "z"
"""
import sys
sys.stdin = open("input.txt")

lst = [0 for _ in range(26)]
for s in input():
    idx = ord(s) - 97
    lst[idx] += 1
print(' '.join(map(str, lst)))