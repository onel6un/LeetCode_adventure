from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        list_rows = []
        for n in range(1, numRows + 1):
            curr_row = [1] * n
            if n == 1 or n == 2:
                list_rows.append(curr_row)
                continue
            prev_row = list_rows[n - 2]
            for i in range(n):
                if i == 0 or i == n - 1:
                    continue
                curr_row[i] = prev_row[i - 1] + prev_row[i]
            list_rows.append(curr_row)
        return list_rows


s = Solution()
print(s.generate(3))
