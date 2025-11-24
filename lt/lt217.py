# LeetCode 217 - Contains Duplicate (Easy)
#
# Дан целочисленный массив nums, верни true если какое-либо значение
# встречается как минимум дважды в массиве, и верни false если каждый элемент уникален.
#
# Пример 1:
# Input: nums = [1,2,3,1]
# Output: true
#
# Пример 2:
# Input: nums = [1,2,3,4]
# Output: false
#
# Пример 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
#
# Constraints:
# - 1 <= nums.length <= 10^5
# - -10^9 <= nums[i] <= 10^9


def containsDuplicate(nums):
    return len(nums) != len(set(nums))
