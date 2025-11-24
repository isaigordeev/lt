from lt.lt21 import ListNode, mergeTwoLists


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
list1 = create_list([1, 2, 4])
list2 = create_list([1, 3, 4])
print(f"Test 1: list1=[1,2,4], list2=[1,3,4]")
merged = mergeTwoLists(list1, list2)
print(f"Expected: [1,1,2,3,4,4], Got: {list_to_array(merged)}\n")

# Test case 2
list3 = create_list([])
list4 = create_list([])
print(f"Test 2: list1=[], list2=[]")
merged2 = mergeTwoLists(list3, list4)
print(f"Expected: [], Got: {list_to_array(merged2)}\n")

# Test case 3
list5 = create_list([])
list6 = create_list([0])
print(f"Test 3: list1=[], list2=[0]")
merged3 = mergeTwoLists(list5, list6)
print(f"Expected: [0], Got: {list_to_array(merged3)}\n")
