class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = len(nums)
        if count==0:
            return count
        k = 0
        for x in range(1,len(nums)):
            if nums[k] != nums[x]:
                k += 1
                nums[k] = nums[x]
        del nums[k+1:]
        return k+1


nums = [1]
print Solution().removeDuplicates(nums)
print nums