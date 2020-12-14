class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        short = min(strs, key=len)  # 找最短字符串

        # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
        print(list(enumerate(short)))
        for i, word in list(enumerate(short)):
            for item in strs:
                if item[i] != word:
                    return short[:i]
        return short


if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    solu = Solution()
    print(solu.longestCommonPrefix(strs))