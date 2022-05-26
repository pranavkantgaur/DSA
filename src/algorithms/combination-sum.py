# https://leetcode.com/problems/combination-sum/
from collections import Counter

class Solution:      

    def backtrack(self, state, candidates, target, result):
             if target == 0:
                temp_state = state.copy()
                for a_state in result: # to avoid duplicates
                    if Counter(a_state) == Counter(state):
                        return
                result.append(temp_state)
                return
             else:
                for candidate in candidates:
                    if target - candidate >= 0:
                        state.append(candidate)
                        self.backtrack(state, candidates, target - candidate, result)
                        explored_value = state.pop()
                    else:
                        continue
                return                     

    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        state = []
        self.backtrack(state, candidates, target, result)
        return result
        

        
