class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # l = list(s)
        # result = ''
        # while len(l) > 0:
        #     result += l.pop()
        # return result
        def func(s):
            if len(s) < 1:
                return s
            return func(s[1:]) + s[0]

        return func(s)

nums = 'hello'
print Solution().reverseString(nums)
