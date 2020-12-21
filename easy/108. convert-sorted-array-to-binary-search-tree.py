'''
Author: mxh970120
Date: 2020.12.21
'''

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        n = len(nums)
        mid = n // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root