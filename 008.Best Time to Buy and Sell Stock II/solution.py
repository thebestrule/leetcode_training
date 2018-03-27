class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        count = len(prices)
        if count < 0:
            return 0
        profit = 0
        for i, j in enumerate(prices):
            if i + 1 != count and j < prices[i + 1]:
                profit += prices[i + 1] - j

        return profit







nums = [4,3,6,7,8,9,10,4,6,3,9]
print Solution().maxProfit(nums)
