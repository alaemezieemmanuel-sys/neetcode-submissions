class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashtable = {}
        most = []
        for i in nums:
            if i  not in hashtable:
                hashtable[i] = 1
            else:
                hashtable[i] += 1
            
        while k > 0:
            v = max(hashtable.values())
            for key, value in hashtable.items():
                if value == v:
                    most.append(key)
                    hashtable.pop(key)
                    break
            k -=1
        
        return most

            
        