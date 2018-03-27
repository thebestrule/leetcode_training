class Solution():
    def containsDuplicate(self,nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_set = set(nums)
        if len(nums) == len(num_set):
            return False
        return True


print Solution().containsDuplicate([1,2,4,5,2])