class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        tempList = []
        for i,element in enumerate(nums):
            if element == 0:
                tempList.append(i)
        j = 0
        for element in tempList:
            nums.pop(element-j)
            nums.append(0)
            j += 1



nums = [0,0,1]
Solution().moveZeroes(nums)
print nums