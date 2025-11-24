from lt.lt242 import isAnagram


# Test case 1
s1, t1 = "anagram", "nagaram"
print(f"Test 1: s='{s1}', t='{t1}'")
print(f"Expected: True, Got: {isAnagram(s1, t1)}\n")

# Test case 2
s2, t2 = "rat", "car"
print(f"Test 2: s='{s2}', t='{t2}'")
print(f"Expected: False, Got: {isAnagram(s2, t2)}\n")

# Test case 3
s3, t3 = "listen", "silent"
print(f"Test 3: s='{s3}', t='{t3}'")
print(f"Expected: True, Got: {isAnagram(s3, t3)}\n")
