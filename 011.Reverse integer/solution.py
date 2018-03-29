class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        flag = 1 if x < 0 else 0
        x = abs(x)
        res = 0
        while x > 0:
            res = res * 10 + x % 10
            x /= 10
        if flag:
            res = -res
        if res > 2 ** 31 - 1 or res < -2 ** 31:
            return 0
        return res

        # if (ans > 2 ** 31 - 1) | (ans < -2 ** 31):
        #     return 0
        # return nums


nums = -456456356
print Solution().reverse(nums)