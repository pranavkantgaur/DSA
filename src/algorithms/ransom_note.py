'''
Given two strings, one representing a ransom note and the other representing the available letters from a magazine, determine if it's possible to construct the ransom note using only the letters from the magazine. Each letter from the magazine can be used only once.
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # get the freq. of letters in mag.
        hmap = {}
        for letter in magazine:
            if letter in hmap:
                hmap[letter] += 1
            else:
                hmap[letter] = 1
        # reduce the letter freq. of randomnote
        for letter in ransomNote:
            if letter in hmap and hmap[letter] > 0:
                hmap[letter] -= 1
            else:
                return False     
        # return true if complete substraction is possible
        return True
