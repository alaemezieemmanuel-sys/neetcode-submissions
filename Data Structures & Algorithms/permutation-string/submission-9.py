class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        index1= 0
        have = {}
        need = {}
        havelen = 0
        needlen = len(set(s1))
        for i in s1:
            need[i] = need.get(i, 0) + 1

        for index2 in range(len(s2)):
            char = s2[index2]
            have[char] = have.get(char, 0) + 1
            
            if  char in need and need[char] == have[char]:
                havelen+=1
            
            if char in need and  have[char] == need[char]+1:
                havelen-=1

            if index2 - index1 + 1 == len(s1):
                if havelen == needlen:
                    return True
                if s2[index1] in need and need[s2[index1]] == have[s2[index1]]:
                    havelen-=1
                have[s2[index1]] -= 1
                if s2[index1] in need and need[s2[index1]] == have[s2[index1]]:
                    havelen+=1
                index1+=1



        return False 
        
        