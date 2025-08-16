# without / and O(n)


nums = [1, 2, 3, 4]


# 1 2 3 4  nums

# 1 3 
# 2 4 

# 2 1 
# 4 3 


# res[i] = r_l[i] * l_r[i] = nums[i-1] * r_l[i-1] * nums[i+1] * r_l[i+1] 


def prod(nums):
    r_l = nums[:]
    r_l[-1] = 1

    l_r = nums[:]
    l_r[0] = 1

    # l[i] = l[i-1]*nums[i+1]
    # l[i] = l[i

    for i in range(1, len(nums)):
        l_r[i] = l_r[i-1] * nums[i-1]

    for i in range(len(nums)-1, 0, -1):
        r_l[i-1] = r_l[i] * nums[i]

    
    return [x*y for x,y in zip(l_r, r_l)]


