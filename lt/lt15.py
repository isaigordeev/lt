# LeetCode 15 - 3Sum (Medium)
#
# Дан целочисленный массив nums, верни все триплеты [nums[i], nums[j], nums[k]]
# такие что i != j, i != k, и j != k, и nums[i] + nums[j] + nums[k] == 0.
#
# Обрати внимание, что набор решений не должен содержать дубликаты триплетов.
#
# Пример 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Объяснение:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
#
# Пример 2:
# Input: nums = [0,1,1]
# Output: []
#
# Constraints:
# - 3 <= nums.length <= 3000
# - -10^5 <= nums[i] <= 10^5

from .lt1 import twoSum1


def threeSum(nums: list):
    _res = set()
    _treated_target = set()
    _treated_target.add(0)

    for i, _target in enumerate(nums):
        if _target not in _treated_target:
            _a, _b = twoSum1(
                nums[:i] + nums[i + 1 :], -1 * _target
            )  # inverted

            if _a:
                _res.add(
                    (
                        _a,
                        _b,
                        _target,
                    )
                )

            _treated_target.add(_target)
            _treated_target.add(_target * -1)
        else:
            continue

    return _res
