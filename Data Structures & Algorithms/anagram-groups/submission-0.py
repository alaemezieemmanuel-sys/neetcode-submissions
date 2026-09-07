class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        index = 0
        hashmap = {}
        output = []
        while index < len(strs):
            current = strs[index]
            sorted_current = "".join(sorted(current))
            if sorted_current in hashmap:
                hashmap[sorted_current].append(current)
            else:
                hashmap[sorted_current]= []
                hashmap[sorted_current].append(current)
            index +=1
        for key, value in hashmap.items():
            output.append(value)
        return output
            
            

            
        