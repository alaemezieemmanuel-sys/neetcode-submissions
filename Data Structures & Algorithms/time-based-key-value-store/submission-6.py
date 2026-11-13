class TimeMap:

    def __init__(self):
        self.data = {} 

        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append([value, timestamp])

        
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        values = self.data.get(key,  [])

        i1, i2 = 0, len(values) - 1

        while i1 <= i2:
            mid = (i1 + i2) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                i1 = mid + 1

            else:
                i2 = mid - 1
                

        return res
            
                                
        

            

        
