class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [0, 0]
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                result = [i, j]
                if nums[i] + nums[j] == target:
                    return result