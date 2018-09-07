class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = 0
        output = []
        carry = 1
        while carry == 1:
            if digits[-i] + carry == 10:
                output.insert(0, 0)
                i += 1
            else:
                carry = 0
                
            if digits[len(digits)-1-i] + carry == 10:
                carry = 1
                digits[-i] = 0
                i += 1
            else:
                digits[len(digits)-1-i] += carry
                carry = 0
                i += 1
        return digits
