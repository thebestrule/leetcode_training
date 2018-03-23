class Solution():
    def containsDuplicate(self,nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        t = dict()
        for x in nums:
            if x in t.keys():
                t[x] += 1
                if t[x] > 1:
                    return True
            else:
                t[x] = 1

        return False


print Solution().containsDuplicate([1,2,4,5,2])