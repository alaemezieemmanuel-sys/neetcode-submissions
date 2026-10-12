class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ommission =0 
        index1 = 0
        index2= 0
        maxi = 0
        hashmap = {}

        while index2< len(s):
            window_length = index2 - index1 + 1
            r = s[index2]

            if r in hashmap:
                hashmap[r] += 1 
            else:
                hashmap[r] = 1

            if window_length - max(hashmap.values()) <= k:
                maxi = max(maxi, window_length)
            else:
                hashmap[s[index1]] -=1
                index1+=1
            index2+=1
        
        return maxi

