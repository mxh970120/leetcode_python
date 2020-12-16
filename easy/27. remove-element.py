'''
Author: mxh970120
Date: 2020.12.15
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if val not in nums:
            return len(nums)
        i = 0
        while i < len(nums):
            if val == nums[i]:
                nums.pop(i)
            else:
                i += 1
        return i


if __name__ == '__main__':
    nums = [3,2,2,3]
    val = 3
    solu = Solution()
    print(solu.removeElement(nums, val))