# https://medium.com/@rohitverma_87831/decoding-googles-coding-interview-20b1f8fcaf66
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
LCA: 


                    a

                b       c

            d      e

(a, b) -> a
(b, c) -> a
(d, e) -> b


Approach: TC: O(nlogn), SC: O(n)
1. Check if root is LCA of p, q, return root
2. Else, if p,q both in a subtree, either left or right: call lca function on left/right subtree and pass the returned lca_node upwards.


# binary tree and 2 node LCA is to be found.
def getLCANode(root, p, q): -> lca_node
    if root == None or root == p or root == q: return root
    p_in_left = nodeExists(root.left, p)
    q_in_left = nodeExists(root.left, q)
    if p_in_left != q_in_left: return root
    if p_in_left: # both p, q in left subtree
        return getLCANode(root.left, p, q)
    else:
        return getLCANode(root.right, p, q)
        
# binary tree and k-node LCA is to be found:
                    a

                b       c

            d      e

(a, b, c), k = 3 -> a
(d, b, c), k = 3 -> a
(d, e, b), k = 3 -> b

# Approach: TC: O(knlogn), SC: O(n)
1. Check if root node is one of the input node, return root as LCA: O(k)
2. Check if some input nodes exist in left subtree but not all: return root: O(k * n)
3. If all nodes exist in left subtree: call lca on root.left: 
4. If none nodes exist in left subtree: call lca on root.right

def nodeExists(root, node):
    if root == None: return False
    if root == node: return True
    return nodeExists(root.left, node) or nodeExists(root.right, node)

def getLCANode(root, nodes_list):
    if root == None or root in nodes_list: return root
    node_in_left_tree = False
    node_exist_count = 0
    for node in nodes_list:
        node_exist_count += 1 if nodeExists(root.left, node) else 0
    if node_exist_count == len(nodes_list):
        return getLCANode(root.left, nodes_list)
    elif node_exist_count == 0:
        return getLCANode(root.right, nodes_list)
    else:
        return root

# n-nary tree with k-node LCA is to be found:
                                a

                b                   c                           d

        f      d      e         g         h      k          l       m

(f, e, c), n  = 4, k = 3 -> a
(f, d, b), k = 3 -> b
(e, h, m), k = 3 -> a

# approach:
1. check if root is none or in the nodes_list: return root
2. check if any of the children contains all but atleast 1 node: return root
3. there is one child having all nodes: return getlca(child, nodes_list)


def getLCA(root, nodes_list):
    if root is None or root in nodes_list: return root
    for child in root.children:
        node_ctr = 0
        for node in nodes_list:
            node_ctr += 1 if nodeExists(node, child) else 0
        if node_ctr == len(nodes_list): return getLCA(child, nodes_list)
        if nodes_ctr == 0: continue
        else: return root
