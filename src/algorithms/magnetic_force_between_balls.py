# https://leetcode.com/problems/magnetic-force-between-two-balls/
class Solution:

    def predicate(self, max_min_force_th, n_balls, position):
        # return true if n_balls could be places to have atleast max_min_force_th as the maximum minimun force between them.
        # select m baskets such that the resulting min_max >= min_max_force_th, if such a m-basket tuple is found return true, else false.
        # if we can get the count of number of balls that could be placed if the min. distance between them is max_min_force_th and it turns out to be = n_balls then we can return true        
        i = 0
        prev_pos = 0
        n_balls = 1 # assuming first ball is placed at first basket
        while(i < len(position)):
            if position[i] - position[prev_pos] >= max_min_force_th:
                prev_pos = i
                n_balls += 1
                if n_balls == max_min_force_th:
                    return True
            else:
                i += 1    
        return False


    def maxDistance(self, position: List[int], m: int) -> int:
        '''
        position = [1,2,3,4,7], m = 3
        [1, 2, 3] = f = 1
        1-4-7, f = 3
        1-3-7, f = 2
        2-4-7, f = 2
        BF: n^m * n, selecting m baskets from n and evaluating min force between two balls.
        range of f is from 1 to 3
        binary search in this range:
        for a cand. f (mid), check if min-force  = mid is possible, if yes, then shift left to mid + 1 else, shift right to mid - 1
        '''
        left = min([position[i + 1] - position[i] for i in range(len(position) - 1)])# min. possible force between 2 balls = min(pos[i] - pos[j])
        right = position[-1] - position[0] # max force possible
        print(f'left: {left}, right: {right}')
        while(left < right):
            #mid = left + (right - left) // 2
            mid = right - (right - left) // 2
            if self.predicate(mid, m, position):
                left = mid
            else:
                right = mid - 1
        return left
        
