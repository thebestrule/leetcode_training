class Solution:
    def plusOne(self, digits):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # count = len(digits)
        # if count > 1:
        #     digits.reverse()
        # t = 1
        # for i, x in enumerate(digits):
        #     r = x + t
        #     if r == 10:
        #         digits[i] = 0
        #         if i == count - 1:
        #             digits.append(1)
        #             break
        #
        #     else:
        #         digits[i] = r
        #         t = 0
        #         break
        #
        # digits.reverse()
        # return digits
        carry=1
        for i in range(len(digits)-1, -1, -1):
            digits[i]+=carry
            if digits[i] > 9:
                digits[i]-=10
                carry=1
            else:
                carry=0
            if carry == 0:
                break
        if carry == 1:
            digits.insert(0, 1)
        return digits

nums = [9,9,9,9,8]

print Solution().plusOne(nums)
