# https://leetcode.com/problems/basic-calculator/
class Solution:
    def apply_operator(self, operator, operand):
        oper = operator.pop()
        op2 = operand.pop()
        op1 = operand.pop()
        if oper == '+':
            op = op1 + op2
        if oper == '-':
            op = op1 - op2
        operand.append(op)
        return 

    def calculate(self, s: str) -> int:
        operand = []
        operator = []
        i = 0
        while(i < len(s)):
            if s[i] == ' ':
                i += 1
                
            elif s[i].isdigit():
                num = 0
                while(i < len(s) and s[i].isdigit()):
                    num = num*10 + int(s[i])
                    i += 1
                operand.append(num)
                
            elif s[i] in '+-':
                while(len(operator) and operator[-1] != '('):
                    self.apply_operator(operator, operand)
                operator.append(s[i])
                i+=1
            elif s[i] == '(':
                operator.append(s[i])
                i += 1
            else:
                while(operator[-1] != '('):
                    self.apply_operator(operator, operand)
                operator.pop()
                i += 1
        while(len(operator)):
            self.apply_operator(operator, operand)
        return operand.pop()
