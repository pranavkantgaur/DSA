# https://leetcode.com/problems/basic-calculator/
class Solution:
    def apply_operator(self, operator, operand):
        oper = operator.pop()
        op2 = operand.pop()
        if oper == '#': # unary -
            operand.append(-1*op2)
            return
        op1 = operand.pop()      

        if oper == '+':
            op = op1 + op2
        if oper == '-':
            op = op1 - op2
        operand.append(op)
        return 
    
    def is_unary(self, s, i):        
        while(i > 0 and s[i - 1] == ' '):
            i -= 1
        if i == 0 or s[i - 1] in '+-(': return True # it is unary if on an operator is present on the left side of it       
        
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
                if len(operator) and operator[-1] == '#':
                    num *= -1
                    operator.pop()
                operand.append(num)
                
            elif s[i] in '+-':     
                if s[i] == '-' and self.is_unary(s, i):
                    operator.append('#')
                    i += 1
                    continue
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
