class Solution:
    dct_r = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def _nmbr_to_arbc(self, nmbr):
        return self.dct_r.get(nmbr)

    def romanToInt(self, roman: str) -> int:
        number = 0
        for indx, rmn_nmbr in enumerate(roman):
            curr_arb_nmbr = self._nmbr_to_arbc(rmn_nmbr)
            if indx < len(roman) - 1:
                nxt_arbc_nmbr = self._nmbr_to_arbc(roman[indx + 1])
                if nxt_arbc_nmbr <= curr_arb_nmbr:
                    number += curr_arb_nmbr
                else:
                    number -= curr_arb_nmbr
            else:
                number += curr_arb_nmbr
        return number


s = Solution()
print(s.romanToInt('LVIII'))