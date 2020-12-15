class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 利用了python的特性
        # return haystack.find(needle)

        m, n = len(haystack), len(needle)
        for i in range(m - n + 1):
            if haystack[i:i + n] == needle:
                return i
        return -1


if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"
    solu = Solution()
    print(solu.strStr(haystack, needle))