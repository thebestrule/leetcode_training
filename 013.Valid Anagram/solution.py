class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        slen = len(s)
        tlen = len(t)
        if slen != tlen:
            return False

        memo = dict()
        for i in s:
            if i not in memo:
                memo[i] = 1
            else:
                memo[i] += 1

        r = []
        for i in t:
            if i in memo and memo[i] > 0:
                r.append(i)
                memo[i] -= 1

        if len(r) == slen:
            return True
        else:
            return False



s = 'ba2a'
t = "aba2"
print Solution().isAnagram(s,t)
