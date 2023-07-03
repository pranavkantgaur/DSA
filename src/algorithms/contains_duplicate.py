'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

class Solution:
    def containsDuplicate(self, nums):
      hashSet = set()
      for element in nums:
        if element in hashSet:
          return True
        else:
          hashSet.add(element)          
      print('Hashset: ', hashSet)
      return False
