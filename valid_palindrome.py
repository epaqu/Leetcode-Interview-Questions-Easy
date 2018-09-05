class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
        
        for c in s:
            if c not in alphabet:
                s = s.replace(c, "")
        if s == s[::-1]:
            return True
        else:
            return False
