'''
s1 : 대상 문자열을 계속 자르기
s2 : 대상 문자열의 slicing index를 10단위씩 늘리기
    - slicing의 끝 부분을 없는 index로 해도 오류가 없음 !
      ex) 'yeramii'[2:100] = 'ramii'
'''
import sys
sys.stdin = open('input.txt')

# s1
s = input()
while True:
    if len(s) >= 10:
        print(s[:10])
        s = s[10:]
    else:
        print(s)
        break

# s2
s = input()
i = 0
while i < len(s):
    print(s[i:i+10])
    i += 10