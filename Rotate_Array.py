class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        temp = nums[0:len(nums)-k]
        del nums[0:len(nums)-k]
        nums.extend(temp)
