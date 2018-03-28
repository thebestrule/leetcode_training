class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return set(s) == set(t) and all(s.count(i) == t.count(i) for i in set(s))
        sset = set(s)
        tset = set(t)

        if sset != tset:
           return False
        for x in sset:
            if s.count(x) != t.count(x):
                return False

        return True

s = 'ba2a'
t = "aba2"
print Solution().isAnagram(s,t)
