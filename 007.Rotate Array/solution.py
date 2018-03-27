class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # count = len(nums)
        # for i,j in enumerate(nums):
        #     if i > k:
        #         break
        #     nums[i], nums[count-k+i-1] = nums[count-k+i-1],nums[i]
        n = len(nums)
        k = k % n
        nums[:k], nums[k:] = nums[n-k:], nums[:n-k]

nums = [1,2,3,4,5,6,7]
k = 3
Solution().rotate(nums,k)
print nums
