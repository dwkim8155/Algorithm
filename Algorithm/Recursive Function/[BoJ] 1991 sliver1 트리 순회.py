N = int(input())

tree=dict()

for _ in range(N):
    root, left, right = input().split()
    tree[root] = (left, right)

def pri(root):
    if root != ".":
        print(root, end="")
        pri(tree[root][0])
        pri(tree[root][1])

def mid(root):
    if root != ".":
        mid(tree[root][0])
        print(root, end="")
        mid(tree[root][1])

def post(root):
    if root != ".":
        post(tree[root][0])
        post(tree[root][1])
        print(root, end="")


for f in [pri, mid, post]:
    f("A")
    print()

