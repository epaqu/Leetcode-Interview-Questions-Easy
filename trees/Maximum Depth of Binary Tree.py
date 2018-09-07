# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if root.left and root.right:
            return max(Solution.maxDepth(self, root.left), Solution.maxDepth(self, root.right))+1
        elif not root.left:
            return Solution.maxDepth(self, root.right)+1
        else:
            return Solution.maxDepth(self, root.left)+1
