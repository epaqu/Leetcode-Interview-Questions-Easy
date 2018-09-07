import random
class Solution(object):
    # Your Solution object will be instantiated and called as such:
    # obj = Solution(nums)
    # param_1 = obj.reset()
    # param_2 = obj.shuffle()
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.__orig = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.__orig

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        shuffled = []
        indices = []
        for i in range(0, len(self.__orig)):
            indices.append(i)
        random.shuffle(indices)
        for i in indices:
            shuffled.append(self.__orig[i])
        return shuffled
        


