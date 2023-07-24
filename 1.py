
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if 2 > len(nums) or len(nums) > 10**4 or -10**9 > target or target > 10**9:
            return
        for i_n, nmbr in enumerate(nums):
            if -10**9 > nmbr > 10**9:
                return
            i_o = 0
            while i_o < len(nums):
                if nmbr + nums[i_o] == target and i_o != i_n:
                    return [i_n, i_o]
                i_o += 1


s = Solution()
a = range(1, 10001)
print(len(a))
print(s.twoSum(a, 19999))
