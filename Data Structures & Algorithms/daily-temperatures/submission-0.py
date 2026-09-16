class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        days=[0 for _ in range(len(temperatures))]
        for index, temperature in enumerate(temperatures):
            while  len(stack) > 0 and temperature > temperatures[stack[-1]] :
                days[stack[-1]] = index - stack[-1]
                stack.pop()
            stack.append(index)

        return days
            
                


            
        