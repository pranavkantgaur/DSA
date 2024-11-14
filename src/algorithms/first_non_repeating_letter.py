'''
Given a string, identify the position of the first character that appears only once in the string. If no such character exists, return -1.
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # create hmap letter:first_index -- O(n), reset val for letter to invalid if letter repeats
        hMap = {}
        for index, letter in enumerate(s):
            if letter in hMap:
                hMap[letter] = -1
            else:
                hMap[letter] = index
        # scan hmap for key with min. value -- O(n)
        min_index = len(s) + 1
        for letter in hMap:
            if hMap[letter] != -1 and hMap[letter] < min_index:
                min_index = hMap[letter]
        return -1 if min_index == len(s) + 1 else min_index

