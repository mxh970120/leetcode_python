'''
Author: mxh970120
Date: 2020.12.22
'''
import collections

# 和107类似，多了一层奇偶性检测
class Solution:
    def zigzagLevelOrder(self, root):

        res = list()
        index = 1
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
            # 当index为奇数时，就正向输出
            if (index & 1) == 1:
                res.append(level)
            # 当index偶位数时，就反向输出，即先调用一次reverse，再保存
            else:
                res.append(level[::-1])
            index += 1

        return res



