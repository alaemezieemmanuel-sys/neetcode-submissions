class Solution:
    def isHappy(self, n: int) -> bool:
        total  = 0
        visited = set()
        while True:
            n = str(n)
            for i in n:
                total+=((int(i))**2)
            if total == 1:
                return True
            if total in visited:
                return False
            visited.add(total)
            n=total
            total=0
        