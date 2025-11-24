# LeetCode 21 - Merge Two Sorted Lists (Easy)
#
# Даны heads двух отсортированных связных списков list1 и list2.
# Объедини два списка в один отсортированный список.
#
# Пример 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
# Пример 2:
# Input: list1 = [], list2 = []
# Output: []
#
# Пример 3:
# Input: list1 = [], list2 = [0]
# Output: [0]
#
# Constraints:
# - Количество узлов в обоих списках в диапазоне [0, 50]
# - -100 <= Node.val <= 100
# - Оба списка отсортированы в неубывающем порядке


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    # TODO: implement
    pass
