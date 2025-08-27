# ##  #
# ######## #
############


###

height = [9,6,8,8,5,6,3]

def fill_water(heights):


    heights = [0, *heights, 0]
    borders = []
    filled_ = 0

    i, j = 1, 2

    left_max, right_max = heights[i], heights[j]

    while i < len(heights) and j > 0:
        if i == j:
            left_max = max(left_max, heights[i])
        if heights[j] < heights[i]:
            j += 1
        else:
            right_max = heights[j]
            capacity_ = max(left_max, heights[j])
            filled_ += max(capacity_ - heights[i], 0)
            i += 1








if __name__ == "__main__":
    filled_ = fill_water(height)

    print(filled_)
