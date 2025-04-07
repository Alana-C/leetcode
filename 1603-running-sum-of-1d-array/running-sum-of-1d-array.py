class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running_sum_list = []
        total = 0
        for number in nums:
            total += number
            running_sum_list.append(total)
        return running_sum_list