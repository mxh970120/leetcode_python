class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        # 既然要尽可能的大，那么这个数从高位开始要尽可能地保持不变。那么我们找到从高到低第一个满足
        # str[i] > str[i + 1]的位置，然后把
        # str[i] - 1, 再把后面的位置都变成99....即可。
        # 注意str[i] - 1 < str[i-1] 的情况

        if N < 10: return N
        num = list(str(N))
        n = len(num)
        index = -1
        # 找到第一个从高到低满足str[i] > str[i + 1]的位置
        for i in range(0, n-1):
            if num[i] > num[i+1]:
                index = i
                break
        # 判断这一位和前一位的数字是否相同，如果相同，则向高位移动一位,首位则跳过该步
        while num[index] == num[index-1] and index != 0:
            index -= 1

        num[index] = str(int(num[index]) - 1)

        # index 没有发生变化
        if index == -1:
            return N

        for i in range(index + 1, n):
            num[i] = '9'

        return int("".join(num))




if __name__ == '__main__':
    N = 101
    solu = Solution()
    print(solu.monotoneIncreasingDigits(N))