class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        index = 0
        for letters in zip(*strs):
            if len(set(letters)) == 1:
                index += 1
            else:
                break
        return strs[0][0:index]
