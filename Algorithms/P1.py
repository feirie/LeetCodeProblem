class Solution(object):
    #brute force
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx_outer,item in enumerate(nums):
            for idx_inner in range(idx_outer+1,len(nums)):
                if item+nums[idx_inner] == target:
                    return [idx_outer+1,idx_inner+1]
