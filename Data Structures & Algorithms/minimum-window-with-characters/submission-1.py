class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0:
            return  ""
        index1= 0
        have = 0
        need = len(set(t))

        res, resLen= [-1,-1], float("infinity")

        window ={}
        norm = {}

        for i in t:
            norm[i]=norm.get(i,0) +  1


        for index2 in range(len(s)):
            char = s[index2]

            window[char] = window.get(char, 0) + 1

            if char in norm and window[char] == norm[char]:
                have+=1
            
            while have == need:
                if resLen > (index2 - index1 + 1):
                    res = [index1,index2]
                    resLen = (index2 - index1 + 1)
                window[s[index1]] -=1
                if s[index1] in norm and window[s[index1]] < norm[s[index1]]:
                    have-=1
                index1+=1
        
        return s[res[0]: (res[1] + 1)]
