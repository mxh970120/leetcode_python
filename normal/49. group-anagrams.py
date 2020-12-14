class Solution:
    def groupAnagrams(self, strs):
        res = {}
        for item in strs:
            k = ''.join(sorted(item))  # 字符串排序，Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
            print(k)
            if k not in res:  # 判断是否存在
                res[k] = []
            res[k].append(item)  # 相同字符串放到同一个字典的键key中
            print(res)
        return [res[x] for x in res]  # 输出结果


if __name__ == '__main__':
    strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    solu = Solution()
    print(solu.groupAnagrams(strs))