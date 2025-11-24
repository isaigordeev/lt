from lt.lt53 import maxSubArray


# Test case 1
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Test 1: {nums1}")
print(f"Expected: 6, Got: {maxSubArray(nums1)}\n")

# Test case 2
nums2 = [1]
print(f"Test 2: {nums2}")
print(f"Expected: 1, Got: {maxSubArray(nums2)}\n")

# Test case 3
nums3 = [5, 4, -1, 7, 8]
print(f"Test 3: {nums3}")
print(f"Expected: 23, Got: {maxSubArray(nums3)}\n")
