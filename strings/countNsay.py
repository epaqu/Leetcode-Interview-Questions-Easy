class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        else:
            prev = Solution.countAndSay(self, n-1)
            result = ""
            i = 0
            while i < len(prev):
                numOFnum = 1
                for j in range(i+1, len(prev)):
                    if prev[i] == prev[j]:
                        numOFnum += 1
                        i += 1
                    else:
                        break
                result = result + str(numOFnum) + prev[i]
                i += 1
            return result
