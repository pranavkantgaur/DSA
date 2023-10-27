# Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of the same length.
class Solution:
  def findWordConcatenation(self, str1, words):
    result_indices = []
    # TODO: Write your code here
    return result_indices
    '''
    1. store hashmap of word freq, for input word list
    2. run sliding window with incremnets of k, k = len of word
    3 for each new word between last right and current right pointer, update hashmap by decrementing the counter
    4. if current word is not in hash counter, update left = current word + 1
    5. contnue to advance right += 1
    6. if at any point matched == len of counter, add current left pointer to result list
    '''
