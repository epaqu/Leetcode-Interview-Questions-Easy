class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str

        #loop
        output = ""
        for i in range(1, len(s)+1):
            output += s[-i]
        return output
        
        #recursive
        if len(s)<2:
            return s
        return s[-1] + Solution.reverseString(self, s[:-1])
        """
        
        return s[::-1]
