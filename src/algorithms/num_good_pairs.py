#Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

class Solution:
  def numGoodPairs(self, nums):
    pairCount = 0
    numHash = {}    
    for num in nums:
      if num in numHash.keys():
        pairCount += numHash[num]
        numHash[num] += 1
      else:
        numHash[num] = 1       
    return pairCount
