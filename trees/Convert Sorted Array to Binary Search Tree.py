# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def createTree(self, nums):
        node = None
        if 0 < len(nums):
            node = TreeNode(0)
            idx = len(nums) // 2
            node.val = nums[idx]
            node.left = self.createTree(nums[:idx])
            node.right = self.createTree(nums[idx+1:])
        return node
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.createTree(nums)
