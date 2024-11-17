'''
Given a string, determine the length of the longest palindrome that can be constructed using the characters from the string. You don't need to return the palindrome itself, just its maximum possible length.
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:      
        length = 0      
        hmap = {}
        oneRecorded = False
        for letter in s:
            if letter in hmap:
                hmap[letter] += 1
            else:
                hmap[letter] = 1                    
        for letter in hmap:
            if hmap[letter] % 2 == 0:
                length += hmap[letter]
            else:
                length += hmap[letter] - 1
                if not oneRecorded:
                    length += 1
                    oneRecorded = True
        return length

