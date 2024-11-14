from collections import defaultdict

'''
Given a string, determine the maximum number of times the word "balloon" can be formed using the characters from the string. Each character in the string can be used only once.
'''
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:        
        hMap = {}
        for letter in text:
            if letter in hMap:
                hMap[letter] += 1                
            else:
                hMap[letter] = 1
        unique_letters = {'b', 'a', 'l', 'o', 'n'}
        if set(unique_letters).issubset(set(text)): # if all letters are in the input string
            min_count = float('inf')
            for letter in unique_letters:
                if letter in {'b', 'a', 'n'}:
                    if min_count > hMap[letter]:
                        min_count = hMap[letter]
                else:
                    if min_count > float(hMap[letter] // 2):
                        min_count = hMap[letter] // 2
            return min_count
        else:
            return 0
        

