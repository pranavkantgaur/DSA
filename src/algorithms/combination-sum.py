class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        identify minimum element combination which sums to target, lets say with length 'n'
        test all combinations of length n - 1 to check if they sum to target, if yes append to list
        continue till n-k = len(candidates)
        1. Understand the problem
           1.1. Unknown? Number of combinations which sum to target
           1.2. Data? given array of unique integers and a target integer, number of such combinations which sum to target are bounded
                Any number of repeitions of an integer are permissable
           1.3  Condition: ??
           1.4. Possible to satisfy condition?:  ??
           1.5. Condition sufficient to determine the unknown: ??
           1.6. 
        2. Devise plan:(DFS with backtracking(when sum >= target))
           2.1. Find connection between data and unknown
                Create node representing state of sum of all combinations as a list(of size 150) where list[i] represents current sum of ith combination
                Update list for each combination by either DFS/BFS, if sum after updation goes > target, remove item from list
                At any time, size of list is <= 150
                If for combination i, sum == target, append the combination to result to list
                2.1.1. At each node in state-space, if sum < target: consider all available numbers for summation 
                2.1.2. Continue untill sum >= target
        3. Carrying out plan:
           visit_queue = [] 
           # what will be the design of the queue:
           Each node in the quue will contain: Current sequence + current sum?
           
           result = []
           # start at root,
           for action in actions: # initialize root of the exploration tree
            visit_queue.push(action.value)
           # start exploration
           while(visit_queue):
            visit_node = visit_queue.pop()
            for action in actions:
                if visit_node.sum + actions.val < target:
                    visit_node.sum += actions.val
                    visit_queue.push(visit_node)
                elif visit_node.sum + actions.val == target:
                    result.append(visit_node.sequence)
                else:                    
                    # discard visit_node by not re-adding it to the visit queue
                    
                
           
           
           
           while(visit_list):
            for num in input_list: # for each available action
                if visit_list[i].sum + num.val < target: 
                    visit_list[i] = visit_list[i].sum + num
                elif visit_list[i].sum + num.val > target:
                    visit_list.pop(i)
                else:
                    result_list.append(visit_list[i])
                    # mark this combination as visited in visit_list
                                
                    
                                    
                                    
                                    
                
        4. Looking back
        '''
        
