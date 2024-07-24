# dummy node (head node) 필요
class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = self    # 처음 생성은 빈 dummy node이니까, next나 prev라 모두 자신 Node를 가리킴
        self.prev = self

# 양방향 연결 리스트의 정보를 요약한 클래스
class DoublyLinkedList:
    def __init__(self):
        self.head = Node()  # dummy node
        self.size = 0

    def __iter__(self):
        v = self.head.next
        while v != self.head:
            yield v
            v = v.next
    def __str__(self):
        return "".join(str(v.key) for v in self)

    def __len__(self):
        pass

    def splice(self, a, b, x):  # Node a, b, x => O(1) : 6개의 link만 수정
        # 조건 1 : ap -> a -> ... -> b -> bn
        # 조건 2 : a와 b 사이에 head node X, x node X
        # 연산 : a~b 까지를 떼어내서 x 다음으로 연결
        # 결과 : ap -> bn -> ... -> x -> a -> ... b -> xn
        if not a or not b or not x: return
        # node 끼리 꼬이지 않기 위해 미리 정의!
        ap = a.prev
        bn = b.next
        xn = x.next
        # 바꿀 것 : ap.next, bn.prev, x.next, a.prev, b.next, xn.prev
        ap.next = bn
        bn.prev = ap
        x.next = a
        a.prev = x
        b.next = xn
        xn.prev = b

    # 이동 연산 -> O(1) : splice 연산을 사용하므로 동일한 시간 복잡도
    def moveAfter(self, a, x):
        # Node a를 Node x 다음으로 이동
        self.splice(a, a, x)

    def moveBefore(self, a, x):
        # Node a를 Node x 전으로 이동
        self.splice(a, a, x.prev)

    # 삽입 연산 -> O(1) : splice 연산을 사용하므로 동일한 시간 복잡도
    def insertAfter(self, x, key):
        # key 값의 새로운 Node를 x 다음에 삽입
        self.moveAfter(Node(key), x)

    def insertBefore(self, x, key):
        # key 값의 새로운 Node를 x 전에 삽입
        self.moveBefore(Node(key), x)

    def pushFront(self, key):
        self.insertAfter(self.head, key)

    def pushBack(self, key):
        self.insertBefore(self.head, key)

    # 탐색 연산
    def search(self, key):  # O(n) : n개의 노드를 갖는 이중 연결 리스트
        v = self.head   # dummy node
        while v.next != self.head:  # 한 바퀴 돌 때 까지만 진행
            if v.key == key:
                return v
            else:
                v = v.next
        return None

    # 삭제 연산 -> O(1) : remove를 사용하므로 모두 동일한 시간 복잡도
    def remove(self, x):    # O(1) : 2개의 link만 바꿈
        # Node x를 삭제
        # 기존 : xp -> x -> xn
        # 변경 : xp -> xn
        if x == None or x == self.head:
            return
        x.prev.next = x.next
        x.next.prev = x.prev
    # 5라는 Node를 없애고자 할 때, search(5) 결과를 remove() 인자로 넘겨야 함

    def popFront(self):
        # head(dummy)의 next를 pop
        if self.head.next == None:
            return
        self.remove(self.head.next)

    def popBack(self):
        # head(dummay)의 prev를 pop
        if self.head.prev == None:
            return
        self.remove(self.head.prev)

def join(self):
    # 연결 리스트를 합치기
    pass

def split(self, n):
    # Node n을 기준으로 연결 리스트를 나누기
    pass

