class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            if i == ")" or i == "}" or i == "]":
                if len(stack) == 0:
                    return False
                v = stack.pop()
                if v == "[" and i == "]":
                    continue
                elif v == "{" and i == "}":
                    continue
                elif v == "(" and i == ")":
                    continue
                else:
                    return False
        if len(stack) == 0:   
            return True 
        else:
            return False            
        