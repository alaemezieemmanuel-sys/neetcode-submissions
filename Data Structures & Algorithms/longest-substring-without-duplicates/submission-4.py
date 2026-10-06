class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest= 0
        i = 0
        hashmap = {}
        for j in range(len(s)):
            char = s[j]

            if char in hashmap:
                i = max(hashmap[char] + 1,i)


            hashmap[char] = j
            substring_length = (j-i+1)
            longest = max(longest, substring_length)
        return longest