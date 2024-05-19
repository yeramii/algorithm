"""
Pass - 46924KB 216ms

stable sort vs. unstable sort
    - stable (python 지워)
        - 입력 받은 값들 중에 같은 값이 있는 경우 해당 값의 순서를 그대로 유지
            ex) [[1, 2, 3(X), 4, 5, 3(Y)] -> [1, 2, 3(X), 3(Y), 4, 5]
        - 종류 : Insert Sort, Merge Sort, Bubble Sort, Counting Sort
    - unstable
        - stable한 정렬을 장담하지 않는다.
        - 종류 : Selection Sort, Heap Sort, Quick Sort

In-place sort vs. Not In-place sort
    - In-place
        - 정렬 과정에서 추가적인 메모리를 사용하지 않음
        - 종류 : Insert Sort, Selection Sort, Bubble Sort, Heap Sort, Quick Sort
    - Not In-place
        - 정렬 과정에서 추가적인 메모리를 사용
        - 종류 : Merge Sort, Counting Sort, Radix Sort

sorted(iterable, /, *, key=None, reverse=False)
    - key는 iterable에서 정렬의 기준이 되는 비교 키로, lambda 함수로 지정할 수 있다.
        ex) sorted(iterables, key=lambda x: x[0]) : 첫 번째 항목을 기준으로 정렬
    cf) sort(*, key=None, reverse=False)
        ex) iterables.sort(key=lambda x: x[0])
"""
import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
data = []
for _ in range(N):
    age, name = sys.stdin.readline().split()
    data.append((int(age), name))
for user in sorted(data, key=lambda x: x[0]):
    print(user[0], user[1])