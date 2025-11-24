from lt.lt217 import containsDuplicate


# Test case 1
nums1 = [1, 2, 3, 1]
print(f"Test 1: {nums1}")
print(f"Expected: True, Got: {containsDuplicate(nums1)}\n")

# Test case 2
nums2 = [1, 2, 3, 4]
print(f"Test 2: {nums2}")
print(f"Expected: False, Got: {containsDuplicate(nums2)}\n")

# Test case 3
nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(f"Test 3: {nums3}")
print(f"Expected: True, Got: {containsDuplicate(nums3)}\n")
