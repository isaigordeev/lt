# LeetCode 141 - Linked List Cycle (Easy)
#
# Дан head односвязного списка, определи есть ли в нем цикл.
# Цикл в списке есть, если можно снова достичь какого-то узла,
# непрерывно следуя по указателю next.
#
# Пример 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Объяснение: Цикл в списке, где хвост соединяется со вторым узлом.
#
# Пример 2:
# Input: head = [1,2], pos = 0
# Output: true
#
# Пример 3:
# Input: head = [1], pos = -1
# Output: false
#
# Constraints:
# - Количество узлов в списке в диапазоне [0, 10^4]
# - -10^5 <= Node.val <= 10^5
# - pos равен -1 или допустимому индексу в связном списке


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head):
    # TODO: implement (Floyd's Cycle Detection - Fast & Slow pointers)
    pass
