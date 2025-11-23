# LeetCode 3 - Longest Substring Without Repeating Characters (Medium)
#
# Дана строка s, найди длину самой длинной подстроки без повторяющихся символов.
#
# Пример 1:
# Input: s = "abcabcbb"
# Output: 3
# Объяснение: Ответ "abc", длина 3.
#
# Пример 2:
# Input: s = "bbbbb"
# Output: 1
# Объяснение: Ответ "b", длина 1.
#
# Пример 3:
# Input: s = "pwwkew"
# Output: 3
# Объяснение: Ответ "wke", длина 3.
#
# Constraints:
# - 0 <= s.length <= 5 * 10^4
# - s состоит из английских букв, цифр, символов и пробелов


def lengthOfLongestSubstring(s):
    _curr_set = []
    _max_set_len = 0

    for _ch in s:
        if _ch not in _curr_set:
            _curr_set.append(_ch)
            _l = len(_curr_set)

            if _l > _max_set_len:
                _max_set_len = _l

        else:
            # do increase lenght but order
            _idx = _curr_set.index(_ch)
            _curr_set = _curr_set[_idx + 1 :]
            _curr_set.append(_ch)

    return _max_set_len
