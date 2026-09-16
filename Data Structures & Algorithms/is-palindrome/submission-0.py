import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstring = re.sub(r'[^A-Za-z0-9]', '', s)
        

        p1 =0
        p2 = len(newstring) -1

        while p1 < p2:
            if newstring[p1].lower() == newstring[p2].lower():
                p1 +=1
                p2-=1
            else:
                return False
        return True
        