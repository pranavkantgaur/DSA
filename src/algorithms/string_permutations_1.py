# String with distinct letters, to be permuted and arranged in lexicographical order
# https://www.geeksforgeeks.org/problems/permutations-of-a-given-string2041/1
#User function Template for python3

class Solution:
    def find_permutation(self, S):
        def helper(input_str, current_str, result):    
            if len(input_str) == 2:
                result.append(current_str + input_str)        
                result.append(current_str + input_str[::-1])
                return
            for id, letter in enumerate(input_str): # abcd
                subprob_str = input_str[:id] + input_str[id + 1:]     # bcd
                current_str += letter
                helper(subprob_str, current_str, result) # (bcd, a, [])->[bcd, bdc, cbd, cdb, dbc, dcb]
                current_str = current_str[:-1]
        
        current_str = ""
        result = []  
        S = ''.join(sorted(S))
        helper(S, current_str, result)  
        return result

        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		ans.sort()
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends
