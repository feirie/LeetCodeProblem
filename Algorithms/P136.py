class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for num in nums:
            ret =ret ^ num
        return ret

#test
nums = [1,23,1]
print(Solution().singleNumber(nums))