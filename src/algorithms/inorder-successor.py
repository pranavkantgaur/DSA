# https://www.pramp.com/challenge/MW75pP53wAtzNPVLPG2b

#########################################################
# CODE INSTRUCTIONS:                                    #
# 1) The method findInOrderSuccessor you're asked      #
#    to implement is located at line 30.                #
# 2) Use the helper code below to implement it.         #
# 3) In a nutshell, the helper code allows you to       #
#    to build a Binary Search Tree.                     #
# 4) Jump to line 88 to see an example for how the      #
#    helper code is used to test findInOrderSuccessor.  #
#########################################################

'''
Brute force:
*  Do in-order traversal:
     stop when input-node is visited
       return the successor
* Algo for in-order traversal:
  * start at root
    * put left, right child in queue
      * inorder(root.left)
      * print root.val
      * inorder(root.right)
    * when input node as no child:
      * print node.value
      * pop node from queue
      * return 
    * when inputnode has no left child:
      * print node.value
      * inorder(node.right)
def inorder(node):
  if node == None:
    return 
  else:
    inorder(node.left)
    print(node.value)
    inorder(node.right)
---
Worst case. 
* T: O(n), n: number of nodes in the tree       
  S: O(stack size for recursive function call): stack size = depth of BST,
  for unbalanced BST, O(n)
'''




# A node 
class Node:

  # Constructor to create a new node
  def __init__(self, key):
    self.key = key 
    self.left = None
    self.right = None
    self.parent = None

# A binary search tree 
class BinarySearchTree:

  # Constructor to create a new BST
  def __init__(self):
    self.root = None 


    
  def get_first_node_inorder(self, inputNode):
    if inputNode == None:
      return None
    else:
      #print('Key:', inputNode.key)
      firstNode = self.get_first_node_inorder(inputNode.left)
      if firstNode is None:
        return inputNode
      else:
        return firstNode      
    
    
  def find_in_order_successor(self, inputNode):
    if inputNode.right == None:
      ancestor = inputNode.parent
      while(ancestor is not None and ancestor.key < inputNode.key):
        ancestor = ancestor.parent
      return ancestor  
    else:
      '''
      find first node in inorder traversal of subtree rooted at inputNode.right
      '''
      return self.get_first_node_inorder(inputNode.right)

      
      
      
  # Given a binary search tree and a number, inserts a
  # new node with the given number in the correct place
  # in the tree. Returns the new root pointer which the
  # caller should then use(the standard trick to avoid 
  # using reference parameters)
  def insert(self, key):
    
    # 1) If tree is empty, create the root
    if (self.root is None):
      self.root = Node(key)
      return
        
    # 2) Otherwise, create a node with the key
    #    and traverse down the tree to find where to
    #    to insert the new node
    currentNode = self.root
    newNode = Node(key)
    while(currentNode is not None):
      
      if(key < currentNode.key):
        if(currentNode.left is None):
          currentNode.left = newNode;
          newNode.parent = currentNode;
          break
        else:
          currentNode = currentNode.left;
      else:
        if(currentNode.right is None):
          currentNode.right = newNode;
          newNode.parent = currentNode;
          break
        else:
          currentNode = currentNode.right;

  # Return a reference to a node in the BST by its key.
  # Use this method when you need a node to test your
  # findInOrderSuccessor function on
  def getNodeByKey(self, key):
    
    currentNode = self.root
    while(currentNode is not None):
      if(key == currentNode.key):
        return currentNode
        
      if(key < currentNode.key):
        currentNode = currentNode.left
      else:
        currentNode = currentNode.right
        
    return None
        
######################################### 
# Driver program to test above function #
#########################################

# Create a Binary Search Tree
bst  = BinarySearchTree()
bst.insert(20)
bst.insert(9);
bst.insert(25);
bst.insert(5);
bst.insert(12);
bst.insert(11);  
bst.insert(14);    

# Get a reference to the node whose key is 9
test = bst.getNodeByKey(12)

# Find the in order successor of test
succ = bst.find_in_order_successor(test)
#bst.get_first_node_inorder(test)
# Print the key of the successor node
if succ is not None:
    print ("\nInorder Successor of %d is %d " \
            %(test.key , succ.key))
else:
    print ("\nInorder Successor doesn't exist")
