'''
입력한 대로 출력하는 문제

readline() : 파일의 한 줄을 가져와 문자열로 반환. 파일 포인터는 그 다음 줄로 이동

readlines() : 파일 내용 전체를 가져와 리스트로 반환. 각 줄은 문자열 형태의 리스트의 요소로 저장
    - return : ['~\n', '~\n', '~'] <- 마지막 항목 제외하면 모두 '\n' 이 붙음
    - s1 : 40 ms

read() : 파일 내용 전체를 가져와 하나의 문자열로 반환. 각각의 줄은 \n으로 구분.
    - s2 : 36ms

'''
import sys
sys.stdin = open('input.txt')

# s1
lines = sys.stdin.readlines()
for line in lines:
    print(line, end='')

# s2
print(sys.stdin.read())