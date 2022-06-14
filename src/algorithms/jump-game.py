# https://leetcode.com/problems/jump-game/
'''
Base condition: if nextpos == lastpos: return True, if nextpos > lastpos: return false
for each nextpos in range(a[I]): if jumpgame(nextpos, lastpos): return true.   Outside for loop: return false
'''
