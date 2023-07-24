class Solution:
    def reverse(self, str):
        if not str:
            return ''
        a = str[-1]
        return a + self.reverse(str[:-1])

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return self.reverse(str(x)) == str(x)

s = Solution()
print(s.isPalindrome(21))