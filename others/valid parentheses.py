class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        if len(s) < 2:
            return False
        order = []
        for c in s:
            if c == "(":
                order += "("
            elif c == "{":
                order += "{"
            elif c == "[":
                order += "["
            elif len(order) > 0:
                if c == ")":
                    if order[-1] != "(":
                        return False
                    else:
                        order = order[0:len(order)-1]
                elif c == "}":
                    if order[-1] != "{":
                        return False
                    else:
                        order = order[0:len(order)-1]
                elif c == "]":
                    if order[-1] != "[":
                        return False
                    else:
                        order = order[0:len(order)-1]
            else:
                return False
        if len(order) > 0:
            return False
        return True
