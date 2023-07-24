class Solution(object):
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        i = -1
        letter = s[i] 
        while letter == " ":
            i -= 1 
            letter = s[i]
        count = 0
        try:
            while letter != " ":
                count += 1
                i -= 1
                letter = s[i]
        except IndexError:
            return count
        return count


s = Solution()
print(s.lengthOfLastWord('a '))
