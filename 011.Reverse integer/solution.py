class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = str(abs(x))
        res = 0
        for i,j in enumerate(l):
            res += (10**i) * int(j)

        if x < 0:
            res = -res
        if res > 2 ** 31 - 1 or res < -2 ** 31:
            return 0
        return res

        # if (ans > 2 ** 31 - 1) | (ans < -2 ** 31):
        #     return 0
        # return nums


nums = -153423456456456356
print Solution().reverse(nums)