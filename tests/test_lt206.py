from lt.lt206 import ListNode, reverseList


def create_list(vals):
    if not vals:
        return None
    head = ListNode(vals[0])
    curr = head
    for val in vals[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# Test case 1
head1 = create_list([1, 2, 3, 4, 5])
print(f"Test 1: [1,2,3,4,5]")
reversed1 = reverseList(head1)
print(f"Expected: [5,4,3,2,1], Got: {list_to_array(reversed1)}\n")

# Test case 2
head2 = create_list([1, 2])
print(f"Test 2: [1,2]")
reversed2 = reverseList(head2)
print(f"Expected: [2,1], Got: {list_to_array(reversed2)}\n")

# Test case 3
head3 = create_list([])
print(f"Test 3: []")
reversed3 = reverseList(head3)
print(f"Expected: [], Got: {list_to_array(reversed3)}\n")
