# https://leetcode.com/problems/basic-calculator/
class Solution:
    def calculate(self, s: str) -> int:
        operand_stack = []
        operator_stack = []
        for letter in s:
            if letter == " ":
                continue
            elif letter in operator:
                while(len(operator_stack) and self.get_precedence(operator_stack[-1]) > self.get_precedence(letter)):
                    operator = operator_stack.pop(-1)      
                    operand_1 = operand_stack.pop(-1)
                    operand_2 = operand_stack.pop(-1)
                    result = self.apply_operator(operator1, operator_2, operand)
                    operand_stack.append(result)
                operator_stack.append(letter)
            else:
                operand_stack.append(letter)
        # process expression in the stack
        while(len(operand_stack) and len(operator_stack)):
                operator = operator_stack.pop(-1)      
                operand_1 = operand_stack.pop(-1)
                operand_2 = operand_stack.pop(-1)
                result = self.apply_operator(operator1, operator_2, operand)
                operand_stack.append(result)
        return operand_stack.pop(-1)
