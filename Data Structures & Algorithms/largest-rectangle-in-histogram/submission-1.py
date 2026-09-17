class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        p1 = 0
        max_area = 0
        stack = []
        while p1 < len(heights):
            while len(stack) >0 and heights[stack[-1]] > heights[p1]:
                height = heights[stack.pop()]
                if len(stack) == 0:
                    width =p1 
                else: 
                    width = p1 - stack[-1] - 1
                if (height*width) >  max_area:
                    max_area = (height*width)
            stack.append(p1)
            p1+=1

        return max_area
        