'''
Author: mxh970120
Date: 2020.12.23
'''
import collections
class Solution:
    def firstUniqChar(self, s):
        frequency = collections.Counter(s)
        for i, ch in enumerate(s):
            if frequency[ch] == 1:
                return i
        return -1






if __name__ == '__main__':
    s = "leetcode"
    solu = Solution()
    print(solu.firstUniqChar(s))