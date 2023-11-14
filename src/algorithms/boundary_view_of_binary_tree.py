# https://www.codingninjas.com/studio/problems/boundary-traversal-of-binary-tree_790725
'''
    Time Complexity: O(N)
    Space Complexity: O(N)

    Where N is the number of nodes in the Binary Tree.
'''

# Binary tree node class for reference.
# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


# Functions to traverse on each part.
def traverseBoundary(root):
    hMap = {}
    queue = []
    queue.append([root, 0])
    # set left and right boundary
    while(len(queue)):
        level_size = len(queue)
        for _ in range(level_size):
            node, id = queue.pop(0)
            if node.left or node.right: # not a leaf
                if id not in hMap: # only first occurance
                    hMap[id] = node.data
            if node.left:
                queue.append([node.left, id - 1])	
            if node.right:
                queue.append([node.right, id + 1])
    # get leaf nodes
    stack = []
    leaf_nodes = []
    stack.append([root, 0])								
    while(len(stack)):
        node, visited = stack[-1]
        if not visited:
            if node.left or node.right:
                if node.left:
                    stack.append([node.left, 0])
            else:
                leaf_node.append(node.data)
            stack[-1][1] = 1 # visited mark	
        else:
            stack.pop(-1)
            if node.right:
                stack.append([node.right, 0])
    left_boundary_dist = sorted([key for key in hMap.keys() if key < 0], reverse = True)
    right_boundary_dist = sorted([key for key in hMap.keys() if key > 0], reverse = True)
    result = []
    result = [root.data]
    for dist in left_boundary_dist:
        result.append(hMap[dist].data)
    for node in leaf_nodes:
        result.append(node.data)
    for dist in right_boundary_dist:
        result.append(hMap[dist].data)
    return result				
