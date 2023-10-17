# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
class Solution:
  def searchTriplets(self, arr):
    triplets = []
    arr.sort()
    for id, num in enumerate(arr):
      if id > 0 and arr[id] == arr[id - 1]:
        continue
      first = id + 1
      last = len(arr) - 1
      target = -1 * num
      while(first < last):
        current_sum = arr[first] + arr[last]
        if current_sum == target:
          triplets.append([num, arr[first], arr[last]])
          first += 1
          last -= 1
        elif current_sum < target:
          first += 1
        else:
          last -= 1
    return triplets
