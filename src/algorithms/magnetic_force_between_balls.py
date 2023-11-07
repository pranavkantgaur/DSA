# https://leetcode.com/problems/magnetic-force-between-two-balls/
class Solution:
    def predicate(self, max_min_force_th, n_balls_th, position):  
        '''
        check if we can place m balls with this force threshold, if yes, return true, else return false.
        '''
        i = 1
        prev_pos = 0
        n_balls = 1 # assuming first ball is placed at first basket
        while(i < len(position)):
            if position[i] - position[prev_pos] >= max_min_force_th:
                prev_pos = i
                n_balls += 1
                if n_balls == n_balls_th:
                    return True
            i += 1    
        return False

    def maxDistance(self, position: List[int], m: int) -> int:

        position.sort()
        left = 0
        right = position[-1] - position[0] # max force possible

        while(left < right):
            #mid = left + (right - left) // 2 # WHY, TLE?
            mid = right - (right - left) // 2
            if self.predicate(mid, m, position):
                left = mid
            else:
                right = mid - 1
        return left
                
