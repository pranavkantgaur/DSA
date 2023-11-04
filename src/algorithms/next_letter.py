# Given an array of lowercase letters sorted in ascending order, find the smallest letter in the given array greater than a given ‘key’.

# Assume the given array is a circular list, which means that the last letter is assumed to be connected with the first letter. This also means that the smallest letter in the given array is greater than the last letter of the array and is also the first letter of the array.

# Write a function to return the next letter of the given ‘key’.
class Solution:
  def searchNextLetter(self, letters, key):
    left = 0
    right = len(letters) - 1
    while(left <= right):
      mid = left + (right - left) // 2
      if letters[mid] > key:
        right = mid - 1
      elif letters[mid] < key:
        left = mid + 1
      else:
        return letters[(mid + 1) % len(letters)]
    return letters[left % len(letters)]
