'''
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing English letters (lower or upper-case), return true if sentence is a pangram, or false otherwise.

Note: The given sentence might contain other characters like digits or spaces, your solution should handle these too.
'''
class Solution:
  def checkIfPangram(self, sentence):
    # TODO: Write your code here
    alphabet_set = set()
    for letter in sentence:
      if letter.isalpha() and letter.isascii():
          alphabet_set.add(letter.lower())        
      else:
        continue          
    print(alphabet_set)
    if len(alphabet_set) == 26:
      return True
    else:
      return False
