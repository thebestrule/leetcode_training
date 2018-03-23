class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int] 
        :rtype: int 
        """
        # l = len(nums)
        # if l == 1:
        #     return nums[0]
        # result = 0
        # for num in nums:
        #     result ^= num
        # return result
        return 2 * sum(set(nums)) - sum(nums)


print Solution().singleNumber([1,2,3,1,2])