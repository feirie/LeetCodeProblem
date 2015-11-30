class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict = {}
        for num in nums:
            dict[num] = dict.get(num,0)+1

        single_num_list = []
        for (num,num_times) in dict.items():
            if num_times == 1:
                single_num_list.append(num)
        return single_num_list


#test
nums = [1, 2, 1, 3, 2, 5]
print( Solution().singleNumber(nums))