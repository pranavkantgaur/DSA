# https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringHMap = {}
        # for each string in input
        for word in strs:
            key = "".join(sorted(word))
            if key not in stringHMap.keys():
                stringHMap[key] = []
            stringHMap[key].append(word)
        return stringHMap.values()              
