from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    """Получает на вход отсортированный список целых чисел
    и находит позицию target в нем, если target нет в nums
    возвращает, предпологаемую позицию"""
    if nums[0] > target:
        return 0
    if target == nums[0]:
        return 0
    len_arr = len(nums)
    pointer = len_arr // 2
    right = len_arr
    left = 0
    while True:
        if left == pointer:
            return pointer + 1
        elif nums[pointer] < target:
            left = pointer
            pointer += (right - left) // 2
        elif nums[pointer] > target:
            right = pointer
            pointer -= ((right - left) + 1) // 2
        else:
            return pointer


print(searchInsert([1], 0))
