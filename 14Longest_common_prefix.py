
class Solution:
    @staticmethod
    def _get_longest_word(words):
        len_word = {}
        for word in words:
            len_word[len(word)] = word
        return len_word[max(len_word)]

    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ''
        lngst_word = self._get_longest_word(strs)
        indx = 0
        while True:
            try:
                letter = lngst_word[indx]
                lst_match = all([True if letter == f_word[indx] else False for f_word in strs])
                if lst_match:
                    prefix = prefix + letter
                    indx += 1
                else:
                    return prefix
            except IndexError:
                return prefix

s = Solution()
print(s.longestCommonPrefix([""])) con