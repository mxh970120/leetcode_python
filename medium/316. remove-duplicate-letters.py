'''
Author: mxh970120
Date: 2020.12.20
'''

import collections

# 好难
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 要求字典序最小--> 贪心
        count = collections.Counter(s)  # 统计每个字符出现的次数
        stack = []  # 初始化栈

        for c in s:
            if c not in stack:
                # 对于每一个字符，如果其对应的剩余出现次数大于 1，我们可以选择丢弃
                # 如果栈中相邻的元素字典序更大，那么我们选择丢弃相邻的栈中的元素。
                while stack and c < stack[-1] and count[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            count[c] -= 1
        return ''.join(stack)



if __name__ == '__main__':
    s = "bcabc"
    solu = Solution()
    print(solu.removeDuplicateLetters(s))