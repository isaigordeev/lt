height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# height = [4, 2, 0, 3, 2, 5]

# ##  #
# ######## #
############

def find_left_border(heights, start_idx):
    for i in range(start_idx, len(heights)-2):
        if heights[i+1] < heights[i]:
            return i

    return -1

def find_right_border(heights, start_idx):
    for i in range(start_idx, len(heights)-1):
        if heights[i+1] > heights[i]:
            return i+1

    return -1

def find_border(heights, start_idx):
    for i in range(start_idx, len(heights)-1):
        if heights[i+1] > heights[i]:
            return i+1

    return -1

def fill_capable(heights, left_border_idx, right_border_idx):
    capacity_ = min(heights[left_border_idx], heights[right_border_idx])
    filled_ = 0
    for i_ in range(left_border_idx, right_border_idx):
        filled_ += ( capacity_ - heights[i_] )

    return filled_





def fill_water(heights):

    i, j = 0, 0
    capable_ = False
    pre_capable_ = False

    filled_ = 0
    capacity_ = 0

    len_ = len(heights)

    left_border_idx_ = 0
    right_border_idx_ = 1

    while True:
        if not pre_capable_:
            left_border_idx_ = find_left_border(heights, left_border_idx_)

            if left_border_idx_ != -1:
                pre_capable_ = True
            else:
                return filled_

        if pre_capable_:
            right_border_idx_ = find_left_border(heights, right_border_idx_)
            if right_border_idx_ != -1:
                capable_ = True
            else:
                return filled_

        if capable_:
            filled_ += fill_capable(heights, left_border_idx_, right_border_idx_)
            pre_capable_ = False
            capable_ = False

            left_border_idx_ = right_border_idx_
            right_border_idx_ += 1



if __name__ == "__main__":
    filled_ = fill_water(height)

    print(filled_)
