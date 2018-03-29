import re
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        newstr = re.findall(r"[A-Z|a-z|\d]",s.lower())
        l = len(newstr)
        for x in range(l):
            k = l - 1 - x
            if k < x:
                break
            if newstr[x] != newstr[k]:
                return False
        return True




nums = 'A man2, a plan, a canal: Pa2nama'
print Solution().isPalindrome(nums)