class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 字符串切片反转
        value = str(x)[::-1]
        if value == str(x):
            return True
        else:
            return False