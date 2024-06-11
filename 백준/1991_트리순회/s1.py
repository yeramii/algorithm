"""
Pass - 31120KB 44ms
"""
import sys
sys.stdin = open("input.txt")

N = int(input())
left = dict()
right = dict()
par = dict()
for _ in range(N):
    p, l, r = input().split()
    left[p] = l
    right[p] = r
    par[l] = p
    par[r] = p

def preorder(v):
    if v != ".":
        print(v, end="")
        preorder(left[v])
        preorder(right[v])
def inorder(v):
    if v != ".":
        inorder(left[v])
        print(v, end="")
        inorder(right[v])
def postorder(v):
    if v != ".":
        postorder(left[v])
        postorder(right[v])
        print(v, end="")
preorder("A")
print()
inorder("A")
print()
postorder("A")
