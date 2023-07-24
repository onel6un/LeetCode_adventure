from typing import Dict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Проверяет является ли два слова аннограммой"""
        return self._get_dict_from_word(s) == self._get_dict_from_word(t)

    def _get_dict_from_word(self, word: str) -> Dict[str, str]:
        dct_ltr = {}
        for ltr in word:
            if ltr in dct_ltr.keys():
                dct_ltr[ltr] += 1
            else:
                dct_ltr[ltr] = 1
        return dct_ltr


s = Solution()
print(s.isAnagram())
