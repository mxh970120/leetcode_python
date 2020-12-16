'''
Author: mxh970120
Date: 2020.12.13
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = roman[s[-1]]
        n = len(s)
        for i in range(n - 1, 0, -1):
            if roman[s[i - 1]] < roman[s[i]]:
                res -= roman[s[i-1]]
            else:
                res += roman[s[i-1]]
        return res