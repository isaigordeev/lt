# LeetCode 1 - Two Sum (Easy)
#
# Дана целочисленный массив nums и целое число target.
# Верни индексы двух чисел так, чтобы их сумма равнялась target.
#
# Можно предположить, что каждый входной массив имеет ровно одно решение,
# и нельзя использовать один и тот же элемент дважды.
#
# Пример:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Объяснение: nums[0] + nums[1] == 9, возвращаем [0, 1]
#
# Constraints:
# - 2 <= nums.length <= 10^4
# - -10^9 <= nums[i] <= 10^9
# - -10^9 <= target <= 10^9


nums = [2, 7, 12, 13, 15]
nums = [13]
target = 26


def twoSum0(nums, target) -> tuple[int, int]:
    for _x in nums:
        for _y in nums:
            if _x + _y == target:
                return (_x, _y)

    return (-1, -1)


def twoSum1(nums, target) -> tuple[int, int]:
    _dict = set()
    for _x in nums:
        if _x not in _dict:
            _dict.add(target - _x)
        else:
            return (_x, target - _x)

    return (-1, -1)


pair = twoSum1(nums, target)

print(pair)
