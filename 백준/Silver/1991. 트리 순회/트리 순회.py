#1991 트리 순회

N = int(input())
tree = {}

for _ in range(N):
  node, left, right = map(str, input().split())
  tree[node] = (left, right)

def pre(node):
  if node == '.' :
    return
  # 노드 왼쪽 오른쪽
  print(node, end='')
  pre(tree[node][0])
  pre(tree[node][1])

def mid(node):
  if node == '.' :
    return
  mid(tree[node][0])
  print(node, end='')
  mid(tree[node][1])

def pos(node):
  if node == '.' :
    return
  pos(tree[node][0])
  pos(tree[node][1])
  print(node, end='')

pre('A')
print("")
mid('A')
print("")
pos('A')
