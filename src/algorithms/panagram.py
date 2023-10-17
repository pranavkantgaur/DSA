# Given a string sentence containing English letters (lower or upper-case), return true if sentence is a pangram, or false otherwise.
class Solution:
  def checkIfPangram(self, sentence):
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
