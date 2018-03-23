class Solution:


    def intersect(self,nums1,nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        memo = dict()
        for i in nums1:
            if i not in memo:
                memo[i] = 1
            else:
                memo[i] += 1

        r = []
        for i in nums2:
            if i in memo and memo[i] > 0:
                r.append(i)
                memo[i] -= 1
        return r


print Solution().intersect([1], [1,1])
print Solution().intersect([1,2,2,1], [2,2])
print Solution().intersect([4,7,9,7,6,7], [5,0,0,6,1,6,2,2,4])