from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# in a nested case it won't work

#   10
#  /  \
# 5   15
#    /
#   6   <- ошибка: 6 < 10, но левый ребёнок 15, код это не заметит

def isvalid(node):

    def traversal(node):
        tree_ = deque([node])

        while tree_:
            curr_node = tree_.popleft()

            if curr_node.left is not None:
                if curr_node.left.val >= curr_node.val:
                    return False
                else:
                    tree_.append(curr_node.left)

            if curr_node.right is not None:
                if curr_node.right.val <= curr_node.val:
                    return False
                else:
                    tree_.append(curr_node.right)

        return True

    return traversal(node)


# Дерево:
#       10
#      /  \
#     5    15
#    / \   / \
#   3   7 12 20

#recursion
def dfs_traversal(node, list_):
    if node is None:
        return

    if node.left:
        dfs_traversal(node.left, list_)

    list_.append(node.val)

    if node.right:
        dfs_traversal(node.right, list_)

    print(list_)
    return list_

def dfs_traversal_without_memory(node, list_):
    if node is None:
        return True

    if node.left:
        if not dfs_traversal_without_memory(node.left, list_):
            return False

    prev = list_[0]
    if prev >= node.val:
        list_[1] = False and list_[1]
        return False
    else:
        list_[0] = node.val
        list_[1] = True and list_[1]

    if node.right:
        if not dfs_traversal_without_memory(node.right, list_):
            return False

    return list_[1]

def issorted(list_):

    for i in range(len(list_) - 1):
        if list_[i] > list_[i + 1]:
            return False

    return True




if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)

    root.left.left = TreeNode(6)
    root.left.right = TreeNode(7)

    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)

    # list_ = dfs_traversal(root, [])
    # print(issorted(list_))

    print(dfs_traversal_without_memory(root, [-float('inf'), True]))


