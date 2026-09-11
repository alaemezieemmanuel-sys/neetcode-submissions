import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        for i in tokens:
            if i not in ["+", "-","*","/"]:
                stack.append(int(i))
            elif i == "+":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1+num2)
            elif i == "-":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif i == "*":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num2 * num1)
            elif i == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(math.trunc(num1/num2))
        return stack[-1]