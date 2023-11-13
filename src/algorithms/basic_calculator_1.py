# https://leetcode.com/problems/basic-calculator/
class Solution:
    def _get_value(self, operator, op1, op2):
        if operator == '+':
            return op1 + op2
        else:
            return op1 - op2

    def _evaluate_operator(self, operand_stack, operator_stack):
        op2 = operand_stack.pop(-1)
        op1 = operand_stack.pop(-1)
        operator = operator_stack.pop(-1)
        new_operand = self._get_value(operator, op1, op2)        
        operand_stack.append(new_operand)

    def calculate(self, s: str) -> int:
        '''
        1. App. 1:
           1. Convert to post-fix: 
              1. Remove all space letters
              2. For every op. 1 <operator> op. 2, transform to op1. op2 <operator>
           2. Evaluate post-fix
        2. App. 2:
           1. Use operator and operand stack to eval. infix.
              1. If precedence of new operator is same or higher as prev. or the stack is empty, push the operator
              2. If precedence is lower than top of stack, the pop the operator and evaluate and push the new operand
              3. Once the input expression is over, then take out the operator in operator stack and a pair of operands from operand stack evaluate and push the result to the operand stack. Continue this untill no operator in the operator stack. Once operator stack is empty return the top of operand stack. 
              4. if '(' is received push to stack
              5. if ')' is received, continue with pop operands and operators till '(' is received in the operator stack(down-stream).
        '''
        operand_stack = []
        operator_stack = []
        operators = ['+', '-']
        open_bracket_counter = 0
        result = 0
        for letter in s:
            if letter == ' ':
                continue
            elif letter in operators:
                if len(operator_stack) - open_bracket_counter > 0: # not checking precedence becuase - and + have same precedence
                    self._evaluate_operator(operand_stack, operator_stack)
                operator_stack.append(letter)
            elif letter == '(':
                operator_stack.append(letter)
                open_bracket_counter += 1
            elif letter == ')':
                while(operator_stack[-1] != '('):
                    self._evaluate_operator(operand_stack, operator_stack)
                operator_stack.pop(-1) # remove '('
                open_bracket_counter += 1
            else:
                operand_stack.append(int(letter))
        while(len(operator_stack)):
            self._evaluate_operator(operand_stack, operator_stack)
        
        if len(operand_stack):
            result = operand_stack.pop(-1)
        
        return result

        
