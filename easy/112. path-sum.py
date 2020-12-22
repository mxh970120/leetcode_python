'''
Author: mxh970120
Date: 2020.12.22
'''

class Solution:
    # 询问是否存在从当前节点 root 到叶子节点的路径，满足其路径和为 sum
    # 递归：满足sum-val1，sum-val2……
    def hasPathSum(self, root):
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        # 是否存在从当前节点的子节点到叶子的路径，满足其路径和为 sum - val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

