# https://leetcode.com/problems/text-justification/
'''
BF: 
1. Pack as many words as possible with one space in between untill total characters is less than max words:
2. if adding next word increases length beyond max words per line, delay adding that word for next line and
3. add remainig space between selected words for this line in left to right order.

TC: ? SC: ??
'''

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        for word in words:
            line = []
            current_len = 0
            while current_len + word + 1 < maxWidth:
                line.append(word + ' ')
            else:
                line = addSpace(line, maxWidth - len(line))
            result.append(line)
        return result            
                
