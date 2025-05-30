class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = {}
        for i in s:
            count[i] = count.get(i, 0) + 1
        for i in t:
            count[i] = count.get(i, 0) - 1
            if count[i] == -1:
                return i