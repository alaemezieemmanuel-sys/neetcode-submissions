class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        total = 0
        if 1 > len(operations) or len(operations) > 1000:
            return "Can't Work"
        for i in operations:
            if i not in ["+", "D", "C"]:
                record.append(int(i))
            elif i == "+":
                if len(record) < 2:
                    return "Can't Work"
                num2 = record.pop()
                num1 = record.pop()
                record.append(num1)
                record.append(num2)
                record.append(num1+num2)
            elif i == "D":
                if len(record) == 0:
                    return "Can't Work"
                record.append((record[-1])*2)
            elif i == "C":
                if len(record) == 0:
                    return "Can't Work"
                record.pop()
        while len(record) > 0:
            a = record.pop()
            total+=a

        return total
            
