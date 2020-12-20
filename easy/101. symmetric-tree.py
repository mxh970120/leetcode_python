'''
Author: mxh970120
Date: 2020.12.19
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def symmetric(self, p, q):
        if p is None and q is None:
            return True
        if p and q and p.val == q.val:
            return self.symmetric(p.left, q.right) and self.symmetric(p.right, q.left)
        return False

    def isSymmetric(self, root):

        if root:
            return self.symmetric(root.left, root.right)
        return True
