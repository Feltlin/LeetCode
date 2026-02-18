class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = 1
        i = 0
        if len(s) == 0:
            return 0
        if s[0] == '-' or s[0] == '+':
            if len(s) == 1:
                return 0
            if s[0] == '-':
                sign = -1
            i = 1
        while s[i] == 0:
            i += 1
        j = i
        while j < len(s) and s[j].isdigit():
            j += 1
        if i == j:
            return 0
        return max(-2**31, min(2**31 - 1, int(s[i : j]) * sign))

        