class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0

        for i,x in enumerate(haystack):
            if x == needle[0]:
                if haystack[i:len(needle)+i] == needle:
                    return i
                else:
                    pass

        return -1



haystack = "mississippi"
needle = "issip"


print Solution().strStr(haystack,needle)

print haystack.find(needle)