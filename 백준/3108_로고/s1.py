"""
Pass - 39140KB 280ms

집합을 만들기 위해서 set 사용
    - 교집합 = s1 & s2 = s1.intersection(s2)
    - 합집합 = s1 | s2 = s1.union(s2)
    - 차집합 = s1 - s2 = s1.difference(s2)
    - 값 1개 추가 : s1.add(4)
    - 값 여러개 추가 : s1.update(lst1)
    - 특정 값 제거 : s1.remove(a)

    cf) dictionary
        - k-v쌍 1개 삭제 : del dict1[key]
        - k-v쌍 모두 삭제 : dict1.clear()

Union-Find
    - 그래프 알고리즘으로, 두 노드가 같은 그래프에 속하는지 판별
    - 노드를 합치는 Union 연산과, 루트 노드를 찾는 Find 연산으로 이뤄짐

나의 풀이
    1) -500~500을 0~1000으로 옮김
    2) -1로 초기화 된 배열에 상자 하나를 그릴 때마다 cnt 올려서 입력
        이 때, 입력하려는 위치가 -1이 아니라면 (겹치는 상자 존재), 해당 상자 번호를 따로 저장 (union)
    3) ans라는 배열에 한 붓 그리기 가능한 상자 번호의 set 들을 삽입하고,
        상자 하나를 다 그릴 때마다 ans에 속한 set 들과 겹치지 않는지 확인
        -> 겹친다면 합집합 처리
    4) 모든 상자를 그린 후, ans에 속한 set의 수를 출력

다른 사람의 풀이 - Union-Find ??

"""
import sys
sys.stdin = open("input.txt")

N = int(input())
arr = [[-1 for _ in range(1001)] for _ in range(1001)]   # zero : 500 500
cnt = 0
arr[500][500] = cnt

def paint_square(x1, y1, x2, y2, cnt):
    global arr
    union = []
    for c in range(x1, x2 + 1):
        if arr[500 + y1][500 + c] != -1:
            union.append(arr[500 + y1][500 + c])
        if arr[500 + y2][500 + c] != -1:
            union.append(arr[500 + y2][500 + c])
        arr[500 + y1][500 + c] = cnt
        arr[500 + y2][500 + c] = cnt
    for r in range(y1 + 1, y2):
        if arr[500 + r][500 + x1] != -1:
            union.append(arr[500 + r][500 + x1])
        if arr[500 + r][500 + x2] != -1:
            union.append(arr[500 + r][500 + x2])
        arr[500 + r][500 + x1] = cnt
        arr[500 + r][500 + x2] = cnt
    union.append(cnt)
    return set(union)

ans = [{0}]
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    cnt += 1
    tmp = paint_square(x1, y1, x2, y2, cnt)
    for i, s in enumerate(ans):
        if tmp & s:
            tmp |= s
    ans2 = [tmp]
    for s in ans:
        if not tmp & s:
            ans2.append(s)
    ans = ans2
print(len(ans)-1)