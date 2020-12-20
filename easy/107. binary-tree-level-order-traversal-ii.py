'''
Author: mxh970120
Date: 2020.12.20
'''

import collections
# 广度优先搜索
class Solution:
    def levelOrderBottom(self, root):
        res = list()
        if not root:
            return res

        # 当层的节点，初始节点
        q = collections.deque([root])
        while q:
            # 该层的值
            level = list()
            size = len(q)
            for _ in range(size):
                # 弹出左侧的节点，弹出len（q）次
                node = q.popleft()
                level.append(node.val)
                # 将下一层的节点加到右侧去
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)

        return res[::-1]

