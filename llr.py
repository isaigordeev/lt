



class Node:
    def __init__(self, next=None, val=0) -> None:

        self.val = val
        self.next = next



root = Node(Node(Node(Node(None, 4), 3), 5), 1)



# while root:
    # print(root.val)
    # root = root.next

def reverse_(node: Node):

    start_ = Node(node)
    
    prev_node = None
    curr_node = node

    while curr_node:
        print(curr_node.val, "val")
        dangled_ = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = dangled_

    print(prev_node.val)
    return prev_node


new_root = reverse_(root)
    
while new_root:
    print(new_root.val, "val")
    new_root = new_root.next
    
