class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            l = int(str(x)[::-1])
        else:
            l = -int(str(abs(x))[::-1])
        if l < -2147483648 or l > 2147483647:
            return 0

        return l



nums = -153423
print Solution().reverse(nums)