# https://practice.geeksforgeeks.org/problems/min-distance-between-two-given-nodes-of-a-binary-tree/1
#User function Template for python3

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def findDist(self,root,a,b):
        def searchNode(root, a_val):
            if root is None: return False
            if root.data == a_val: return True
            return searchNode(root.left, a_val) or searchNode(root.right, a_val)
    
        def getLCA(root, a_val, b_val): # lowest common ancestor
            if root.data in [a_val, b_val]: return root
            a_in_left = searchNode(root.left, a_val)
            b_in_left = searchNode(root.left, b_val)
            if a_in_left != b_in_left: return root
            if a_in_left:
                return getLCA(root.left, a_val, b_val)
            return getLCA(root.right, a_val, b_val)
    
        def bfs(root, a_val, b_val): # (10, 12, 7)
            # search for a_val and b_val
            # return the sum of the distance of both from root
            d_a = -1
            d_b = -1
            queue = [root]
            depth = 0
            while(len(queue)):
                level_size = len(queue)
                for _ in range(level_size):
                    node = queue.pop(0)
                    if node.data in [a_val, b_val]:
                        if node.data == a_val: 
                            d_a = depth
                        else: 
                            d_b = depth
                        if d_a != -1 and d_b != -1: # both a, b are found
                            return d_a + d_b
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                depth += 1
            
    
        if a == b: return 0
        if root.data in [a, b]: 
            lca_node = root        
        else:
            lca_node = getLCA(root, a, b)
        
        return bfs(lca_node, a, b)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(50000)
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root


if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        a, b=map(int, input().split())
        ob = Solution()
        print(ob.findDist(root, a, b))

# } Driver Code Ends
