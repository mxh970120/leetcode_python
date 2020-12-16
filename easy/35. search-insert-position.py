'''
Author: mxh970120
Date: 2020.12.16
'''

class Solution:
    def searchInsert(self, nums, target) -> int:
        # 二分查找
        length = len(nums)
        if length == 0:
            return 0

        # 当target比最大的元素大时，为特殊情况
        if nums[length - 1] < target:
            return length

        # 二分查找边界条件
        left = 0
        right = length - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                # [mid + 1, right]
                left = mid + 1
            else:
                # [left, mid]
                right = mid
        return left

if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 7
    solu = Solution()
    print(solu.searchInsert(nums, target))