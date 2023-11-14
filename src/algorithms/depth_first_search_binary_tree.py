# implement dfs using stack
def dfs_using_stack(root):
  stack = []
  stack.append([root, 0]) # node, visited?
  while(len(stack)):
    node, visited = stack[-1] # peek
    print(node.data)
    if visited:
      if node.left:
        stack.append([node.left, 0])
      stack.pop(-1)
    else:
      stack[-1][1] = 1 # mark visited
      if node.right:
        stack.append([node.right, 0])
  return        
