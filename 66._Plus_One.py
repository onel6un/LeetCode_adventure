from typing import List


class Solution(object):
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            num = digits[i]
            num += 1
            if i == 0 and num > 9:
                digits[i] = 0
                digits.insert(0, 1)
                break
            if num > 9:
                digits[i] = 0
                continue
            digits[i] = num
            break
        
        return digits

s = Solution()
print(s.plusOne([9]))
