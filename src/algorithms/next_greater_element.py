'''
Given an array, print the Next Greater Element (NGE) for every element.

The Next Greater Element for an element x is the first greater element on the right side of x in the array.

Elements for which no greater element exist, consider the next greater element as -1.
'''
class Solution:
    def nextLargerElement(self, arr):
        res = [-1]*len(arr)
        stack = []
        for index, element in enumerate(arr):
            while(stack and element > arr[stack[-1]]):
                res[stack.pop()] = element
            stack.append(index)
        return res
