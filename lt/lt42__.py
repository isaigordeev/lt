height = [4, 2, 0, 3, 2, 5]

# ##  #
# ######## #
############


def find_border(heights, start_idx):
    for i in range(start_idx, len(heights)-1):
        if heights[i+1] < heights[i] and heights[i] > heights[i-1]:
            return i

    return -1

def fill_capable(heights, left_border_idx, right_border_idx):
    capacity_ = min(heights[left_border_idx], heights[right_border_idx])
    filled_ = 0
    for i_ in range(left_border_idx, right_border_idx):
        filled_ += ( capacity_ - heights[i_] )

    return filled_

#  #
## ##
#####

def pick_global(heights, borders):

    peak_heights = heights[borders]

    i, j = 0, 0
    global_heights = heights[borders]


    while i < len(peak_heights):
        if peak_heights[i] < global_heights[i+1]:
            i += 1
        else:






def fill_water(heights):

    left_border_idx_ = 1

    heights = [0, *heights]
    borders = []
    filled_ = 0

    while True:
        border = find_border(heights, left_border_idx_)
        if border == -1:
            break
        else:
            left_border_idx_ = border + 1
            borders.append(border)

    for i_ in range(len(borders)-1):
        filled_ += fill_capable(heights, borders[i_], borders[i_+1])


    return filled_



if __name__ == "__main__":
    filled_ = fill_water(height)

    print(filled_)
