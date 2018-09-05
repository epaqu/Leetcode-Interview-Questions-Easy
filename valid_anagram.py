class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for c in s:
            if c not in t:
                return False
            t = t.replace(c, "", 1)
        if t == "":
            return True
        return False
