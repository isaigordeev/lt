from lt.lt226 import TreeNode, invertTree


def tree_to_array(root, result=None, level=0, index=0):
    """Convert tree to level-order array representation"""
    if result is None:
        result = []

    if root is None:
        return result

    if len(result) <= index:
        result.extend([None] * (index - len(result) + 1))

    result[index] = root.val
    tree_to_array(root.left, result, level + 1, 2 * index + 1)
    tree_to_array(root.right, result, level + 1, 2 * index + 2)

    return result


# Test case 1: [4,2,7,1,3,6,9]
root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(7)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(9)
print(f"Test 1: [4,2,7,1,3,6,9]")
inverted1 = invertTree(root1)
print(f"Expected: [4,7,2,9,6,3,1]")
print(f"Got: {tree_to_array(inverted1)}\n")

# Test case 2: [2,1,3]
root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)
print(f"Test 2: [2,1,3]")
inverted2 = invertTree(root2)
print(f"Expected: [2,3,1]")
print(f"Got: {tree_to_array(inverted2)}\n")

# Test case 3: []
root3 = None
print(f"Test 3: []")
inverted3 = invertTree(root3)
print(f"Expected: []")
print(f"Got: {tree_to_array(inverted3) if inverted3 else []}\n")
