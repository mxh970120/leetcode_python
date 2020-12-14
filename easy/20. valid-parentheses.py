class Solution:
    def isValid(self, s):
        if not s: return True
        if len(s) == 1: return False
        stack = []  # 用栈， 先进后出原则
        parmap = {')': '(', '}': '{', ']': '['}
        for par in s:
            if not stack:
                stack.append(par)
            else:
                if par in parmap:
                    print(par)
                    print(stack)
                    # pop出栈，拿掉最上面（字符串最左边）
                    if parmap[par] != stack.pop():
                        return False
                else:
                    stack.append(par)
        return len(stack) == 0

    # Better answer
    def isValid2(self, s: str) -> bool:
        dic = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            print(stack)
            if stack and i in dic:
                if stack[-1] == dic[i]:
                    print(stack[-1])  # 栈顶
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return not stack



if __name__ == '__main__':
    strs = "{[]}"
    solu = Solution()
    print(solu.isValid2(strs))