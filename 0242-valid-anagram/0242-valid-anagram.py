class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            d.update({s[i] : d.get(s[i], 0) + 1})
            d.update({t[i] : d.get(t[i], 0) - 1})
            if d.get(s[i]) == 0:
                d.pop(s[i])
            if d.get(t[i]) == 0:
                d.pop(t[i])
        return d == {}