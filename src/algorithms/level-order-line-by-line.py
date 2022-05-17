#User function Template for python3

'''
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
'''
 1 4 N 4 2
     
     1
  4     
4   2

o/p: [[1], [4], [4, 2]]



       1
    2     3
4     5  6   7
  8
  
O/P: [[1], [2, 3], [4, 5, 6, 7], [8]]  

'''

'''
1. Visit a node: Print its value
2. Check if no node left in the queue, print $
3. Push children of parent in the queue
4. Continue
'''

#Function to return the level order traversal line by line of a tree.
def levelOrder(root):
    # code here
    queue = []
    results = []
    queue.append(root)
    queue.append(Node('$'))
    results.append([root.data])
    result = []
    while(queue): # BFS termination condition
        node = queue.pop(0)
        if node.data == '$' and len(queue) > 0:            
            results.append(result)
            result = []    
            queue.append(Node('$'))
        if node.left:
    
            queue.append(node.left)
            result.append(node.left.data)
    
        if node.right:
            queue.append(node.right)
            result.append(node.right.data)
    
    return results
#{ 
#  Driver Code Starts
#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

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
        result = levelOrder(root)
        for values in result:
            for value in values:
                print(value,end = " ")
            print("$",end = " ")
        print()


# } Driver Code Ends
