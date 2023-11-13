# practice.geeksforgeeks.org/problems/diagonal-traversal-of-binary-tree/
#User function Template for python3

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
#Complete the function below
class Solution:
    def diagonal(self,root):
        #:param root: root of the given tree.
        #return: print out the diagonal traversal,  no need to print new line
        #code here
        '''
                  1*
           2**            4*
       5***   6**   7**      8*
                        10**    9*
       O= [1, 4, 8, 9, 2, 6, 7, 10, 5]
       
       
                       1*
                2** 
            3***   4**
            O  = [1, 2, 4, 3]
            
            
                  1*
           2**            4*
       5***   6**   7**      8*
                        10**    9*
                              11**
                                  12**
                                      13** 
                                         14**
       O= [1, 4, 8, 9,2, 6, 7, 10, 11, 12, 13, 14, 5]         
       All right nodes copy diag. id from parent and are immidietly printed and left nodes get parent + 1
       When we go to left node, we assing id = parent id + 1 and store it in the hashmap for later printing
       When we go to right node, we assign id = parent id and print it immidietely
        '''
        result = []
        stack = []
        stack.append([root, 0])
        while(len(stack)):
            node, id = stack.pop(-1)
            result.append(node.data)
            if node.right:
                stack.append([node.right, id])
            if node.left:
                hMap[id + 1].append(node.left)
            if not node.left and not node.right:
                del hMap[id][0]
                if len(hMap[id]):
                    stack.append(hMap[id][0])
                else:
                    if id + 1 in hMap:
                        stack.append(hMap[id + 1][0])
                    else:
                        break
        return result
   




#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(50000)
#Contributed by Sudarshan Sharma
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
        obj=Solution()
        diagonalNode = obj.diagonal(root)
        for node in diagonalNode:
            print(node,end=' ')
        print()

# } Driver Code Ends
