# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recursion(self, left, right):
        if left == right == None:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.recursion(left.left, right.right) and self.recursion(left.right, right.left)
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.recursion(root.left, root.right)
    
