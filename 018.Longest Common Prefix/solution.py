class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strsLen = len(strs)
        if not strsLen:
            return ''
        if strsLen == 1:
            return strs[0]
        lens = []
        for x in strs:
            lens.append(len(x))
        minlen = min(lens)
        if minlen == 0:
            return ''
        for x in range(minlen,-1,-1):
            for i,j in enumerate(strs):
                if i == 0:
                    t = j[:x]
                else:
                    t1 = j[:x]

                    if t1 == t:
                        if i + 1 == strsLen:
                            return t
                        else:
                            pass
                    else:
                        break
        return ''

nums = ['aa','aa']
print Solution().longestCommonPrefix(nums)
