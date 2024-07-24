class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None

    def __str__(self):
        return str(self.key)

# 3 -> 9 -> 1 -> None
a = Node(3)     # head node: 모든 노드를 기억할 필요 없이 head node만 기억하고 next로 넘어가면서 찾으면 됨
b = Node(9)
c = Node(-1)
a.next = b
b.next = c

# 기억 방법 : head node, linked list size 의 정보를 담은 class (객체)를 만듬
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def pushFront(self, key):   # O(1) : head를 이미 알고 있으니까
        new_node = Node(key)
        new_node.next = L.head
        L.head = new_node
        L.size += 1

    def pushBack(self, key):    # O(n) : tail을 찾아가야 하니까
        new_node = Node(key)
        if len(self) == 0:
            self.head = new_node
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = new_node
        self.size += 1

    def popFront(self):         # O(1) : head를 이미 알고 있으니까
        if len(self) == 0:
            return None
        else:
            x = self.head
            key = x.key
            self.head = x.next
            self.size -= 1
            del x   # 메모리 상에서 객체를 없앰
            return key

    def popBack(self):          # O(n) : tail을 찾아가야 하니까
        if len(self) == 0:
            return None
        else:
            # running technique : 뒤에서 쫓아가면서 따라가는 것 (prev가 tail을)
            prev, tail = None, self.head
            while tail.next != None:
                prev = tail
                tail = tail.next
            if len(self) == 1:
                self.head = None
            else:
                prev.next = tail.next
            key = tail.key
            del tail
            self.size -= 1
            return key

    def search(self, key):      # O(n) : worst case
        # key 값의 노드를 리턴, 없으면 None 리턴
        v = self.head
        while v != None:
            if v.key == key:
                return v
            v = v.next
        return None

    # for loop를 쓸 수 있도록 yield 키워드로 generator object 생성
    # -> 순차적 자료구조에서는 iterator를 만들어두는 것을 추천
    def __iterator__(self):
        v = self.head
        while v != None:
            yield v     # = return
            v = v.next
        # while 끝나면 StopIterator라는 error message가 자동으로 생성되고, for문에서는 내부적으로 Stop

L = SinglyLinkedList()
L.pushFront(-1)     # -1 -> None
L.pushFront(9)      # 9 -> -1 -> None
L.pushFront(3)      # 3 -> 9 -> -1 -> None
L.pushBack(4)       # 3 -> 9 -> -1 -> 4 -> None
L.popFront()        # 9 -> -1 -> 4 -> None
for x in L:
    print(x)