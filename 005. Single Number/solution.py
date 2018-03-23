class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int] 
        :rtype: int 
        """
        tem = dict()
        for x in nums:
            if x in tem.keys():
                tem[x] += 1
            else:
                tem[x] = 1
        t = list(tem.keys())[list(tem.values()).index(1)]
        return t

print Solution().singleNumber([0])