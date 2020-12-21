'''
Author: mxh970120
Date: 2020.12.21
'''

# 解法1：暴力算法
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
               self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

# 解法2
class Solution:
    # 当节点root 左 / 右子树的高度差 ≥2 ：则返回 -1 ，代表 此子树不是平衡树
    def isBalanced(self, root: TreeNode) -> bool:
        return self.recur(root) != -1

    def recur(self, root):
        if not root:
            return 0

        left = self.recur(root.left)
        if left == -1:
            return -1
        right = self.recur(root.right)
        if right == -1:
            return -1
        # 当节点root 左 / 右子树的高度差 < 2 ：则返回以节点root为根节点的子树的最大高度，即节点 root 的左右子树中最大高度加 1
        if abs(left - right) < 2:
            return max(left, right) + 1
        else:
            return -1

