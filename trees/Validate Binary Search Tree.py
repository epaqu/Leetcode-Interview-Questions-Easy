# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self, root):
        asList = []
        if not root:
            return asList
        asList = Solution.traverse(self, root.left)
        asList.append(root.val)
        asList.extend(Solution.traverse(self, root.right))
        return asList

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        asList = Solution.traverse(self, root)
        if len(set(asList)) == len(asList) and sorted(asList) == asList:
            return True
        return False
