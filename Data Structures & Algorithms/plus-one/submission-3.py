class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        index = len(digits) - 1
        carry = 0
        value = digits[index] + 1
        while index >= 0:
            if value < 10:
                digits[index] = value
                carry = 0
                break
            vbd = value % 10
            carry = value // 10
            digits[index] = vbd
            index-=1
            value = digits[index] + carry
        if carry:
            digits.insert(0,carry)

        return digits
        