'''
Author: mxh970120
Date: 2020.12.17
'''

class Solution:
    def plusOne(self, digits):
        length = len(digits)
        position = length - 1
        carry = False
        digits[-1] += 1
        while position >= 0:
            if carry:
                digits[position] += 1

            if digits[position] >= 10:
                digits[position] -= 10
                carry = True
            else:
                carry = False

            position -= 1
        if carry:
            digits.insert(0, 1)
        return digits



if __name__ == '__main__':
    prices = [4,3,2,1]
    solu = Solution()
    print(solu.plusOne(prices))