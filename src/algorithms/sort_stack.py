# Given a stack, sort it using only stack operations (push and pop).

#You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array). The values in the stack are to be sorted in descending order, with the largest elements on top.

class Solution:
    def sortStack(self,stack):
        temp_stack = []
        temp_stack.append(stack.pop())
        while(stack):
            element = stack.pop()
            while(temp_stack and element < temp_stack[-1]):
                temp_element = temp_stack.pop()
                stack.append(temp_element)
            temp_stack.append(element)

        return temp_stack
