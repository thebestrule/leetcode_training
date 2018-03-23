class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # left = 0
        # for right in range(1, len(nums)):
        #     if (nums[left] == 0):
        #         if (nums[right] == 0):
        #             pass
        #         else:
        #             nums[left] = nums[right]
        #             nums[right] = 0
        #             left += 1
        #     else:
        #         left += 1
        pos = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
            # print i

nums = [5,0,0,1]
Solution().moveZeroes(nums)
print nums