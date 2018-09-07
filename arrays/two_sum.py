class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            if (target - nums[i]) in nums[i+1:]:
                temp = nums[i+1:]
                return [i, temp.index(target - nums[i])+i+1]
