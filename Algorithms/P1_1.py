class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        buff_dict = {}
        for idx,item in enumerate(nums):
            if target-item in buff_dict:
                return [buff_dict[target-item],idx+1]
            buff_dict[item] = idx+1
