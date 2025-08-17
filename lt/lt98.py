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

def issorted_valid(node):

    tree_list_ = deque([node.val])

    def traversal(node):
        tree_ = deque([node])

        while tree_:
            curr_node = tree_.pop()

            if curr_node.left is not None:
                if curr_node.left.val >= curr_node.val:
                    return False
                else:
                    tree_.append(curr_node.left)
                    tree_list_.append(curr_node.left.val)

            if curr_node.right is not None:
                if curr_node.right.val <= curr_node.val:
                    return False
                else:
                    tree_.append(curr_node.right)
                    tree_list_.append(curr_node.right.val)

        return tree_list_

    tree_list_ = traversal(node)
    for i in range(1,len(tree_list_)):
        if tree_list_[i-1] >= tree_list_[i]:
            return False

    return True

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)

    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)

    print(issorted_valid(root))