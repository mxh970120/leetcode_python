'''
Author: mxh970120
Date: 2020.12.25
'''


class Solution:
    def findContentChildren(self, g, s):
        # 首先对数组g和s排序，然后从小到大遍历g中的每个元素，对于每个元素找到能满足该元素的s中的最小的元素。
        g.sort()
        s.sort()
        n, m = len(g), len(s)
        i = j = count = 0
        # 当孩子全被满足或者饼干被分完，循环结束
        while i < n and j < m:
            while j < m and g[i] > s[j]:
                j += 1
            if j < m:
                count += 1
            i += 1
            j += 1

        return count


if __name__ == '__main__':
    g = [1, 2, 3]
    s = [1, 1]
    solu = Solution()
    print(solu.merge(g, s))