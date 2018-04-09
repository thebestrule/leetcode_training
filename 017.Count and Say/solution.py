class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        n = str(n)
        if not n.isalnum():
            return 0
        res = ''
        tmp = 1
        num = len(n)
        for i,x in enumerate(n):
            if num > 2:
                if i != 0:
                    if x == n[i-1]:
                        tmp += 1
                        if num == i + 1:
                            res += str(tmp) + str(x)
                    else:
                        res += str(tmp) + str(n[i-1])
                        tmp = 1
                        if num == i + 1:
                            res += str(tmp) + str(x)
            else:
                res += str(tmp) + str(x)
        return res




nums = 6
print (Solution().countAndSay(nums))
