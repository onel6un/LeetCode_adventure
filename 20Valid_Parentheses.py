class Solution:
    dct_brckt = {')': '(', '}': '{', ']': '['}
    open = ('(', '{', '[')

    def isValid(self, s: str) -> bool:
        stack = []
        for brct in s:
            if brct in self.open:
                stack.append(brct)
            else:
                if not stack or self.dct_brckt[brct] != stack[-1]:
                    return False
                stack.pop(-1)
        if not stack:
            return True
        else:
            return False

s = Solution()

print(s.isValid("(([(())))"))