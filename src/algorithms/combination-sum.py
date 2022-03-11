class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        identify minimum element combination which sums to target, lets say with length 'n'
        test all combinations of length n - 1 to check if they sum to target, if yes append to list
        continue till n-k = len(candidates)
        '''
        
