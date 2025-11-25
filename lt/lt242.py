# LeetCode 242 - Valid Anagram (Easy)
#
# Даны две строки s и t, верни true если t является анаграммой s, и false иначе.
# Анаграмма - слово или фраза, сформированная перестановкой букв другого слова.
#
# Пример 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
#
# Пример 2:
# Input: s = "rat", t = "car"
# Output: false
#
# Constraints:
# - 1 <= s.length, t.length <= 5 * 10^4
# - s и t состоят из строчных английских букв


def isAnagram(s, t):
    return set(s) == set(t)
