# https://leetcode.com/problems/combination-sum/
class Solution:      

    def backtrack(self, state, candidates, target, result):
             if target == 0:
                temp_state = state.copy()
                result.append(temp_state)
                return
             else:
                for index, candidate in enumerate(candidates):
                    if target - candidate >= 0:
                        state.append(candidate)
                        self.backtrack(state, candidates[index:], target - candidate, result)
                        explored_value = state.pop()
                    else:
                        continue
                return                     

    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        state = []
        self.backtrack(state, candidates, target, result)
        return result
        

                

        
