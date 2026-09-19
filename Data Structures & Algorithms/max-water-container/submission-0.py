class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #DEFINING THE INDEXES 
        Index = 0
        Index2 = len(heights) -1

        #DEFINING THE INITIAL HEIGHTS
        height1 = heights[Index]
        height2 = heights[Index2]

        #CALCULATING THE FIRST POSSIBLE AREA
        max_area = min(height1, height2) * (Index2 - Index)

        #LOOP TO CALCULATE ALL AREAS
        while Index < Index2:
            height1 = heights[Index]
            height2 = heights[Index2]
            area = min(height1, height2) * (Index2 - Index)
            if area > max_area:
                max_area = area
            if height1 < height2:
                Index+=1
            else:
                Index2-=1
        return max_area
            
        