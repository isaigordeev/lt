# LeetCode 206 - Reverse Linked List (Easy)
#
# Дан head односвязного списка, разверни список и верни развернутый список.
#
# Пример 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#
# Пример 2:
# Input: head = [1,2]
# Output: [2,1]
#
# Пример 3:
# Input: head = []
# Output: []
#
# Constraints:
# - Количество узлов в списке находится в диапазоне [0, 5000]
# - -5000 <= Node.val <= 5000


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    if not head:
        return []

    curr = head

    _l = []

    while curr.next:
        _next = curr.next
        _next.next = curr
        curr = _next

    while _next:
        _l.append(_next.val)
        _next = _next.next

    return _l
