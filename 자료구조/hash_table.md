[유튜브 강의](https://www.youtube.com/watch?v=Bj4pd9rJp5c)

## Hash Table
- 매우 빠른 **평균** 삽입/삭제/탐색 연산 제공
- hash function을 통해 key를 특정 index에 매핑시키며, 주어진 Table의 해당 index에 (key, value)를 저장
- cf) array는 Table의 0번 index부터 차례대로 저장

### Hash Table 성능을 좌우하는 요소
1. Table 
   - 보통 list로 관리
2. Hash Function
3. Collision Resolution 
   - hash function 결과 index에 이미 다른 값이 있는 경우, 다른 곳에 저장

### Hash Function
- `H`은 Hash Table (list), `m=len(H)` 일 때, H가 m개의 slot을 가진다고 표형
- Division Hash Function
  - `f(k) = k % p % m`
      - `k` : key 값
      - `p` : 소수 (prime number)
      - `m` : hash table 길이
  - 충돌이 일어날 가능성이 큼 (key 별 index가 겹칠 가능성)
- Multiplication / Folding / Mid-Squares / Extraction Hash Function ..
- Perfect Hash Function
  - 충돌이 일어나지 않고, `key:slot = 1:1`로 매핑되는 ideal hash function
- Universal Hash Function
  - `Pr(f(x) == f(y)) = 1/m`
  - 두 개의 서로 다른 key 값에 충돌이 발생할 확률이 전체 hash table 길이에 반비례
  - C-Universal Hash Function
    - `Pr(f(x) == f(y)) = c/m`, (`c`: 상수)
- key 값이 string 일 경우
  - Additive Hash Function
    - `f(k) = sigma(ord(key[i])) % m`
    - key 값의 ascii 값의 총 합 % hash table 길이
  - Rotating Hash Function
    - `h` 값을 계속 업데이트한 뒤, 소수 및 길이로 나눈 값 리턴
    ```python
    h = initial_value
    for i in range(len(key)):
        h = (h << 4) ^ (h >> 28) ^ key[i]   # ^ : exclusive OR
    return h % p % m
    ```
  - Universal Hash Function
    - `h` 값 업데이트를 위와 다르게 함
    - C++의 STL (Standatd Template Library) 및 Java에서 사용 중
    ```python
    h = initial_value
    for i in range(len(key)):
        h = ((h*a) + key[i]) % p
    return h % p % m
    ```
- 좋은 hash function의 기준 (trade-off)
  1. less collision : key값이 여러 slot으로 분산되도록
  2. fast compution

<br>

### Collision Resolution Method (충돌 회피 방법)

1. Open Addressing : 충돌이 일어났다면, 주위의 빈 곳을 찾아서 저장하는 방식
   1) linear probing
   2) quadratic probing
   3) double hashing
2. Chaining


### Linear Probing

- 한 칸씩 밑으로 내려가며 빈 칸을 찾는 방식
- 가정
  - (A5, A2, A3, B5, A9, B2, B9, C2) 순서로 key 값들이 들어오는 상황 
  - table은 circle 처럼 연결되어 있음 (9 -> 0)
- table   
   ```text
   | idx | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |   
   |  H  | B9|   | A2| A3| B2| A5| B5| C2|   | A9|   
                 └        cluster        ┘
   ```
- cluster : key 값들이 연속된 slot에 모여있는 것
- 연산
  - 탐색 = search(key)
    - key값이 매핑된 index부터 내려가며 일치하는 key값 찾으면 return (key, value)
    - 내려가다가 빈칸이 나온다면 table에 저장되지 않았으므로 return None
  - 삽입 = set(key, value=None)
    - key값이 H 내에 있으면 value를 update
    - key값이 H 내에 없으면 (key, value)를 insert
  - 제거 = remove(key)
    - key값을 가진 item을 찾아 slot을 비움

