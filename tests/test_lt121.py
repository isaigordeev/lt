from lt.lt121 import maxProfit


# Test case 1
prices1 = [7, 1, 5, 3, 6, 4]
print(f"Test 1: {prices1}")
print(f"Expected: 5, Got: {maxProfit(prices1)}\n")

# Test case 2
prices2 = [7, 6, 4, 3, 1]
print(f"Test 2: {prices2}")
print(f"Expected: 0, Got: {maxProfit(prices2)}\n")

# Test case 3
prices3 = [2, 4, 1]
print(f"Test 3: {prices3}")
print(f"Expected: 2, Got: {maxProfit(prices3)}\n")
