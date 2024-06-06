"""
Pass - 103176KB 1072ms
    연결 리스트
"""
class Node:
    def __init__(self, key=None):
        self.key = key
        self.prev = self
        self.next = self

    def __str__(self):
        return str(self.key)

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()

    def __iter__(self):
        v = self.head.next
        while v != self.head:
            yield v
            v = v.next

    def __str__(self):
        return "".join(str(v.key) for v in self)

    def splice(self, a, b, x):
        # 기존 : ap -> a -> ... -> b -> bn -> ... -> x -> xn
        # 변경 : ap -> bn -> ... -> x -> a -> ... -> b -> xn
        if a == None or b == None or x == None:
            return
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
    def moveAfter(self, a, x):
        self.splice(a, a, x)
    def moveBefore(self, a, x):
        self.splice(a, a, x.prev)
    def insertBefore(self, a, key):
        self.moveBefore(Node(key), a)
    def deleteNode(self, x):
        if not x or x == self.head:
            return
        x.prev.next, x.next.prev = x.next, x.prev

import sys
sys.stdin = open("input.txt")
L = DoublyLinkedList()
c = Node("|")
c.next = L.head
c.prev = L.head
L.head.next = c
L.head.prev = c
text = list(sys.stdin.readline().strip())
for i in text:
    L.insertBefore(c, i)
N = int(sys.stdin.readline().strip())
for i in range(N):
    cmd = sys.stdin.readline().strip()
    if cmd[0] == "L" and c.prev.key != None:
        L.moveBefore(c, c.prev)
    elif cmd[0] == "D" and c.next.key != None:
        L.moveAfter(c, c.next)
    elif cmd[0] == "B" and c.prev.key != None:
        L.deleteNode(c.prev)
    elif cmd[0] == "P":
        L.insertBefore(c, cmd[2])
L.deleteNode(c)
print(L)

