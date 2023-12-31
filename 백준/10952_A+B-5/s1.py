'''
f-strig 방식과 format() 방식 시간 비교 -> f-string이 빠름

timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000, globals=None)
    주어진 코드 조각에 의해 소요된 실행 시간을 측정하는 Python 표준 라이브러리의 메서드
    (100만번 실행한 뒤 최소 시간을 제공 -> 코드 성능 확인에 유용)
    - stmt : 지정된 코드 조각 (여러 문장 가능)
    - setup : stmt 전에 실행해야 하는 설정 세부 정보
    - timer : Timer 인스턴스 생성
    - number : timeit() 메서드 반복 실행 횟수
    - global : 코드를 실행할 namespace
    - return : [sec]
'''

import sys
sys.stdin = open('input.txt')

T = int(input())
for i in range(1, T+1):
    A, B = map(int, input().split())
    print(f"Case #{i}: {A+B}")
    # print("Case #{}: {}".format(i, A+B))


# 시간 측정
import timeit
tFstring = timeit.timeit('f"{A+B}"', 'A=5\nB=8', number=10000)
tformat = timeit.timeit('"{}".format(A+B)', 'A=5\nB=8', number=10000)
print(tFstring) # 0.0005827001295983791
print(tformat)  # 0.0011076000519096851