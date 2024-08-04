[유튜브 강의](https://www.youtube.com/c/ChanSuShin)

### 연결 리스트 (Linked List) - 한방향 vs. 양방향
- Node : (key, link) 쌍으로 구성
  - key : data 값
    - values : 자료구조에 따라 필요할 겨우 추가
  - link : 다음 주소
    - 한방향 : 1개 (next)
    - 양방향 : 2개 (prev, next)
  - head node : 가장 앞의 노드
- pros and cons
  - pros : insert 연산에서 array보다 효율적
    - array : O(n)
    - linked list : O(1) <- prev/next node를 알고 있다는 가정
  - cons : Node 위치에 따라 위치만큼의 시간 소요
### Singly Linked List
- 한 쪽 방향으로만 연결되면, tail을 알더라도 prev를 알려면 처음부터 찾아야 함 (prev를 tail로 수정하기 위해) -> O(n)
### Circularly Linked List
- tail의 next = head의 prev => 원형 양방향 연결 리스트 (Circularly Doubly Linked List)
- dummy node를 통해 연결 리스트의 시작을 나타냄 (원형 연결 리스트는 시작이 어딘지 모르니까)
  - 시작 노드를 가리키는 marker

  

추후 array / singly linked list / circularly linked list 간에 모든 연산간 시간 복잡도 비교 table 만들어보자!