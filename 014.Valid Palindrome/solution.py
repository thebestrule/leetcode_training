import re
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        newstr = re.findall(r"[A-Z|a-z|\d]",s.lower())
        l = len(newstr) // 2
        if newstr[:l] == newstr[:-(l+1):-1]:
            return True
        else:
            return False


nums = 'A man2, a plan, a canal: Pa2nama'
print Solution().isPalindrome(nums)