class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        sum = 0

        for i in range(len(s) - 1):
            if roman[s[i]] >= roman[s[i + 1]]:
                sum += roman[s[i]]
            else:
                sum -= roman[s[i]]

        return sum + roman[s[-1]]