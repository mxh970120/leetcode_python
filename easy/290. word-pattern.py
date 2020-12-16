'''
Author: mxh970120
Date: 2020.12.16
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        strs = s.split()
        if len(pattern) != len(strs):
            return False
        # 判断plattern是否和s建立映射
        d = dict()
        for i, p in enumerate(pattern):
            if p not in d:
                d[p] = strs[i]
            else:
                if d[p] != strs[i]:
                    return False
        # 判断s和plattern是否建立映射，需要彼此建立映射才一一对应
        d = dict()
        for i, p in enumerate(strs):
            if p not in d:
                d[p] = pattern[i]
            else:
                if d[p] != pattern[i]:
                    return False
        return True


if __name__ == '__main__':
    pattern = "abba",
    str = "dog cat cat dog"
    solu = Solution()
    print(solu.wordPattern(pattern, str))