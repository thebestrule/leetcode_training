class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i,j in enumerate(nums):
            b = target - j
            if b in d.keys():
                x = d[b]
                return [x,i]
            else:
                d[j] = i

print Solution().twoSum([3,4,3], 6)