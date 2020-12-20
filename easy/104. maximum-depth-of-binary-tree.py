'''
Author: mxh970120
Date: 2020.12.20
'''

class Solution:
    def maxDepth(self, root):
        # 深度优先搜索算法 DFS
        # 递归，如果没有节点了说明就到底了，返回0
        if not root:
            return 0
        # 如果还有节点说明还有高度，所以高度+1
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))