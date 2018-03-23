class Solution:


    def intersect(self,nums1,nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        temList = []
        for x in nums1:
            for j,i in enumerate(nums2):
                if x == i:
                    temList.append(x)
                    nums2.pop(j)
                    break
        return temList


print Solution().intersect([1], [1,1])
print Solution().intersect([1,2,2,1], [2,2])
print Solution().intersect([4,7,9,7,6,7], [5,0,0,6,1,6,2,2,4])