class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        index1, index2 =  1, (len(numbers))
        while (index1-1) < (index2 -1):
            result = numbers[index1 - 1] + numbers[index2 - 1]
            if result == target:
                return [index1, index2]
            elif result > target:
                index2 -=1
            else:
                index1+=1
        