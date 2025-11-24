from lt.lt104 import TreeNode, maxDepth


# Test case 1: [3,9,20,null,null,15,7]
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)
print(f"Test 1: [3,9,20,null,null,15,7]")
print(f"Expected: 3, Got: {maxDepth(root1)}\n")

# Test case 2: [1,null,2]
root2 = TreeNode(1)
root2.right = TreeNode(2)
print(f"Test 2: [1,null,2]")
print(f"Expected: 2, Got: {maxDepth(root2)}\n")

# Test case 3: []
root3 = None
print(f"Test 3: []")
print(f"Expected: 0, Got: {maxDepth(root3)}\n")
