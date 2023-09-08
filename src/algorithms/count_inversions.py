'''
# https://www.codingninjas.com/studio/problems/count-inversions_615
Count inversions:
1. For an array with all distinct integers count the number of inversions that may exist among a pair of integers:
arr[i]>arr[j] and i < j

Manual/Naive algorithm: TC-> O(n^2), SC-> O(1)
1. For each number count the inversions it could be part of 
2. Sum total inversions across all numbers
3. Return the sum
'''
