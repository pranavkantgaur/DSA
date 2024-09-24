'''
Given an absolute file path in a Unix-style file system, simplify it by converting ".." to the previous directory and removing any "." or multiple slashes. The resulting string should represent the shortest absolute path.
'''
class Solution:
    def getNextDir(self, path, prev_end):
        start = prev_end
        while(start < len(path) and path[start] == '/'): # skip '/'
            start += 1
        end = start + 1
        while(end < len(path) and path[end] != '/'): # skip till '/'
            end += 1        
        return start, end

    def simplifyPath(self, path):        
        start = 0
        end = 0
        stack = []
        while(end < len(path)):
            start, end = self.getNextDir(path, end)
            if path[start:end] == '..':
                if stack:
                    stack.pop() # pop previous directory name
                else:
                    continue
            elif path[start:end] in ['.', '']:
                continue
            else:                
                stack.append(path[start:end]) # push directory name
        simple_path = '/'.join(stack)
        return '/' + simple_path
