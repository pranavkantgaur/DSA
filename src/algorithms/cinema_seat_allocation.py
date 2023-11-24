# https://leetcode.com/problems/cinema-seat-allocation/
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:       
        reservedSeats.sort(key = lambda seat: seat[0])
        count = 0
        current_row = 1
        index = 0
        a_1, a_2, c = 1, 1, 1
        while(index < len(reservedSeats)):
            while(index < len(reservedSeats) and reservedSeats[index][0] == current_row):
                if 2 <= reservedSeats[index][1] <= 5 and a_1 >0:
                    a_1 -= 1
                if 4 <= reservedSeats[index][1] <= 7 and c > 0:
                    c -= 1
                if 6 <= reservedSeats[index][1] <= 9 and a_2 > 0:
                    a_2 -= 1
                index += 1
            if index == len(reservedSeats): break
            count += max(a_1 + a_2, c) + (reservedSeats[index][0] - current_row - 1) * 2
            a_1, a_2, c = 1, 1, 1
            current_row = reservedSeats[index][0]
        count += max(a_1 + a_2, c) + (n - current_row)* 2
        return count

            


        
