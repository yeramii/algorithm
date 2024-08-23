"""
Pass - 31120KB 44ms

    - str.rjust(width[, fillchar])
        . 오른쪽으로 정렬된 문자열을 왼쪽에 fillchar를 채워서 길이 width인 문자열로 돌려줌.
          fillchar의 기본값은 ASCII 스페이스이며, width가 len(s)보다 작거나 같으면 원래 문자열 반환
        . ex) "11".rjust(3, "0") => "011"
    - str.ljust(width[, fillchar])
    - str.zfill(width)
        . 길이가 width인 문자열을 만들기 위해 ASCII "0"문자를 왼쪽에 채운 문자열의 복사본을 리턴
        . ex) "42".zfill(5) => "00042"
        . ex) "-42".zfill(5) => "-00042"
"""
import sys
sys.stdin = open("input.txt")

N, r, c = map(int, input().split())
rr = bin(r)[2:].rjust(N, '0')
cc = bin(c)[2:].rjust(N, '0')

ans = 0
for i in range(N):
    seq = 0
    if rr[i] == '1':
        seq += 2
    if cc[i] == '1':
        seq += 1
    if not seq: continue
    ans += seq * (2 ** (2 * (N-i-1)))
print(ans)
