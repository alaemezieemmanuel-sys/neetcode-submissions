class Solution:
    def trap(self, height: List[int]) -> int:
        index1 = 0
        index2 = (len(height)) - 1
        total =0
        leftmax = height[index1]
        rightmax = height[index2]
        while index1 < index2:
            if leftmax< rightmax:
                index1+=1
                current_height = height[index1]
                if current_height > leftmax:
                    leftmax= current_height
                else:
                    total += (leftmax-current_height)
                    
            else:
                index2-=1
                current_height = height[index2]
                if current_height > rightmax:
                    rightmax= current_height
                else:
                    total += (rightmax-current_height)
                    
        return total

        