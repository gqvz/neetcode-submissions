class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 2
        digits[-1] += 1
        if digits[-1] != 10:
            return digits
        carry = 1
        digits[-1] = 0
        while i > -1:
            digits[i] += carry
            carry = 0
            if digits[i] == 10:
                digits[i] = 0
                carry = 1
            i -= 1
        if carry == 1:
            digits.insert(0, 1)
        return digits
