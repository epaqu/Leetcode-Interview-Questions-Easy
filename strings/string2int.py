class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        sign=1
        expected=False
        result=0
        for x in str:
            if expected and not x.isdigit():
                break
            if x == "-" and not expected:
                sign *= -1
                expected = True
            elif x == "+" and not expected:
                sign *= 1
                expected = True
            elif x == " ":
                pass
            elif x.isdigit(): #if it is numerical
                result = 10 * result + int(x)
                expected = True
            else:
                break
        result *= sign
        if result > 2**31-1:
            return 2**31-1
        elif result < -2**31:
            return -2**31
        else:
            return result
