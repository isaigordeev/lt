# LeetCode 104 - Maximum Depth of Binary Tree (Easy)
#
# Дан корень бинарного дерева, верни его максимальную глубину.
# Максимальная глубина - количество узлов вдоль самого длинного пути
# от корня до самого дальнего листового узла.
#
# Пример 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
#
# Пример 2:
# Input: root = [1,null,2]
# Output: 2
#
# Constraints:
# - Количество узлов в дереве в диапазоне [0, 10^4]
# - -100 <= Node.val <= 100


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root):
    # TODO: implement
    pass
