# without / and O(n)


nums = [1, 2, 3, 4]
res = copy(nums)

# res[i] = res[i-1]*nums[i+1]

for i, x in range(1, len(res)):
    res[i] = res[i-1] * nums[i+1]

for i, x in range(len(res)-1, 0, -1):
    res[i] = res[i-1] * nums[i+1]
