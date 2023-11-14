# implement dfs using stack
def dfs(root):
  stack = []
  stack.append([root, 0])
  result = []
  while(len(stack)):
	  node, visited = stack[-1]	
	  if visited:
		  if node.left:
			  stack.append([node.left, 0])
		  stack.pop(-1)
	  else:
		  result.append(node.data) # [1, 4 ,5, 2, 3]
		  stack[-1][1] = 1 # mark as visited
		  if node.right:
			  stack.append([node.right, 0])  
