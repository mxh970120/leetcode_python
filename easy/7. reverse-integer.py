class Solution:
    def reverse(self, x: int) -> int:
        isPositiv = True
        if x < 0:
            isPositiv = False
            x = -x
        # 字符串切片反转
        value = str(x)[::-1]
        value = int(value)
        if value > pow(2, 31)-1 or value < -pow(2, 31):
            value = 0

        if isPositiv:
            return value
        else:
            return -value
