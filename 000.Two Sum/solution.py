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
            if b in d.values():
                x = list(d.keys())[list(d.values()).index(b)]
                return [x,i]
            else:
                d[i] = j

