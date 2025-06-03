class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#     1
#    / \
#   2   3
#  / \
# 4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print('-'*50, 'DFS', '-'*50)
# recursive DFS
def dfs(root: Node):
    if not root:
        return
    dfs(root.left)
    dfs(root.right)
    print(root.val)
  
dfs(root)

print('-'*50, 'BFS', '-'*50)
from collections import deque
# BFS
def bfs(root: Node):
    if not root:
        return
    queue = deque([root])
    while queue:
        current = queue.popleft()
        print(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

bfs(root)