class Solution:
    def plusOne(self, digits):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = len(digits)
        if count > 1:
            digits.reverse()
        t = 1
        for i, x in enumerate(digits):
            r = x + t
            if r == 10:
                digits[i] = 0
                if i == count - 1:
                    digits.append(1)
                    break

            else:
                digits[i] = r
                t = 0
                break

        digits.reverse()
        return digits


nums = [9,9,9,9,8]

print Solution().plusOne(nums)
