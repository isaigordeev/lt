# ##  #
# ######## #
############
height = [0,1,0,2,1,0,1,3,2,1,2,1]


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


#  3 2 4 5

def pick_global(heights, borders):

    peak_heights = {i:heights[i] for i in borders}

    i, j = 0, 1
    global_peaks = []

    peak_heights_ =[i_ for i_ in borders]
    while j < len(peak_heights_):
        peak_i = peak_heights[peak_heights_[i]]
        peak_j = peak_heights[peak_heights_[j]]
        if peak_i > peak_j:
            j += 1
        else:
            global_peaks += [peak_heights_[i], peak_heights_[j]]
            i = j
            j += 1


    return global_peaks

def fill_water(heights):

    left_border_idx_ = 1

    heights = [0, *heights, 0]
    borders = []
    filled_ = 0

    while True:
        border = find_border(heights, left_border_idx_)
        if border == -1:
            break
        else:
            left_border_idx_ = border + 1
            borders.append(border)

    borders = pick_global(heights, borders)

    for i_ in range(len(borders)-1):
        filled_ += fill_capable(heights, borders[i_], borders[i_+1])


    return filled_



if __name__ == "__main__":
    filled_ = fill_water(height)

    print(filled_)
