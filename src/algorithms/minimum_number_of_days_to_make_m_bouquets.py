# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        '''
        Binary search over min and max. possible values
        For each mid value check if it is possible to create m buquets with that number of waiting time,
        if yes, attempt to reduce the number of days by setting high = mid, else move to a higher waiting time prediction
        by setting left = mid + 1
        '''
        if len(bloomDay) < m * k:
            return -1

        left = 1#min(bloomDay)
        right = max(bloomDay)
        while(left < right):
            mid = left + (right - left) // 2           
            flow = n_boq = 0
            for day in bloomDay:
                if day <= mid:
                    flow += 1
                    if flow == k:
                        n_boq += 1
                        flow = 0
                        if n_boq == m:
                            break
                else:
                    flow = 0
            if n_boq < m:
                left = mid + 1
            else:
                right = mid
        return left
        
