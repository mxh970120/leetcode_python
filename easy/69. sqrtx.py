'''
Author: mxh970120
Date: 2020.12.18
'''

import math
class Solution:
    def mySqrt(self, x: int) -> int:
        # return int(math.sqrt(x))

        # 二分查找（因为只需要取整）
        if x == 0:
            return 0
        # right: 因为平方根一定小于一半
        left, right = 1, x // 2
        while left < right:
            # 这里一定取右中位数，如果取左中位数，代码可能会进入死循环
            mid = left + (right - left + 1) // 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 < x:
                left = mid
            else:
                right = mid - 1
        return left





if __name__ == '__main__':
    s = 11
    solu = Solution()
    print(solu.mySqrt(s))