'''
Author: mxh970120
Date: 2020.12.15
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i)
            else:
                i += 1
        return i + 1

        # 下面这个算法用了python的特性，但是无法推广
        # nums[:] = sorted(list(set(nums)))
        # return len(nums)


if __name__ == '__main__':
    nums = [1, 1, 2]
    solu = Solution()
    print(solu.removeDuplicates(nums))