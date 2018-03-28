class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # t1 = []
        # t2 = []
        # t3 = []
        # for i,j in enumerate(s):
        #     if j in t1:
        #         k = t1.index(j)
        #         t2[k] += 1
        #     else:
        #         t3.append(i)
        #         t1.append(j)
        #         t2.append(1)
        #
        # if 1 in t2:
        #     return t3[t2.index(1)]
        # else:
        #     return -1

        x = set(s)
        y = []
        for item in x:
            if s.count(item) == 1:
                y.append(s.index(item))
        if len(y) > 0:
            return min(y)
        else:
            return -1

        # seen = {}
        #
        # for l in s:
        #     if l in seen:
        #         seen[l] += 1
        #     else:
        #         seen[l] = 1
        # print seen
        # for i, l in enumerate(s):
        #     if seen[l] == 1:
        #         return i
        #
        # return -1


nums = "bxddec"
print Solution().firstUniqChar(nums)