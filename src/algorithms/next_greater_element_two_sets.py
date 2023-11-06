# Given two integer arrays nums1 and nums2, return an array answer such that answer[i] is the next greater number for every nums1[i] in nums2. The next greater element for an element x is the first element to the right of x that is greater than x. If there is no greater number, output -1 for that number.

# The numbers in nums1 are all present in nums2 and nums2 is a permutation of nums1.

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        # create a monotonically decreasing stack,push elements in nums in a stack:
          # for each current element if it is > than top then pop top and add it to hash map
          # push current element to the stack
          # after the loop, pop all elements of the stack and add hash keys for each
          # iterate through numbers in nums1 and lookup for them in hashmap and return val
        mon_dec_stack = []
        nge_hmap = {}
        for num in nums2:          
          while(len(mon_dec_stack) > 0 and mon_dec_stack[-1] < num):
            # pop the top element
            top = mon_dec_stack.pop(-1)
            # add to hashmap                            
            nge_hmap[top] = num
          mon_dec_stack.append(num)
        while(len(mon_dec_stack)):
          top = mon_dec_stack.pop(-1)
          nge_hmap[top] = -1

        nge_output = []
        for num in nums1:
          nge_output.append(nge_hmap[num])
        return nge_output


