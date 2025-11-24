from lt.lt141 import ListNode, hasCycle


# Test case 1: Cycle at position 1
head1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
head1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Creates cycle
print(f"Test 1: [3,2,0,-4], cycle at pos 1")
print(f"Expected: True, Got: {hasCycle(head1)}\n")

# Test case 2: Cycle at position 0
head2 = ListNode(1)
node2_2 = ListNode(2)
head2.next = node2_2
node2_2.next = head2  # Creates cycle
print(f"Test 2: [1,2], cycle at pos 0")
print(f"Expected: True, Got: {hasCycle(head2)}\n")

# Test case 3: No cycle
head3 = ListNode(1)
print(f"Test 3: [1], no cycle")
print(f"Expected: False, Got: {hasCycle(head3)}\n")
