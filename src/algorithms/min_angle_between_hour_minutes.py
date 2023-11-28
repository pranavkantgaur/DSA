# https://leetcode.com/problems/angle-between-hands-of-a-clock/
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:        
        h_deg = (hour  + minutes / 60)* 30.0
        m_deg = (minutes / 5) * 30.0
        angle_deg_clockwise = abs(h_deg - m_deg)
        return min(angle_deg_clockwise , (360 - angle_deg_clockwise))
        
