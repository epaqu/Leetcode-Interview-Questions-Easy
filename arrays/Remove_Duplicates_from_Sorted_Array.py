class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) > 0:
            comp = nums[0]
            i = 1
            while i < len(nums):
                if nums[i] == comp:
                    del nums[i]
                else:
                    comp = nums[i]
                    i += 1
        return len(nums)
