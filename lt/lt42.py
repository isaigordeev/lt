height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# height = [4, 2, 0, 3, 2, 5]

# ##  #
# ######## #
############


def fill_water(height):

    left_border_h = 0
    right_border_h = 0

    i, j = 0, 0
    capable_ = False
    pre_capable_ = False

    filled_ = 0
    capacity_ = 0

    len_ = len(height)

    while i < len_ - 1:
        if not pre_capable_ and left_border_h >= height[i]:
            i += 1
            print("i", i)
        if not pre_capable_ and left_border_h < height[i]:
            left_border_h = height[i]
            print("i", i, "border", left_border_h)
            pre_capable_ = True
            j = i + 1

        if j < len_ and pre_capable_ and not capable_ and left_border_h >= height[j]:
            print("j", j, height[j])
            j += 1
        elif j < len_ and pre_capable_ and not capable_ and left_border_h < height[j]:
            capable_ = True
            print("j", "right border", height[j])
            capacity_ = min(left_border_h, height[j])

        if capable_:
            cur_filled_ = capacity_ - height[i]
            if cur_filled_ > 0:
                print("i fill", i, height[i], j)
                filled_ += cur_filled_

            i += 1

        if i == j:
            capable_ = False
            pre_capable_ = False
            capacity_ = 0
            left_border_h = 0

        print(capable_, i, j, filled_)

    return filled_


fill_water(height)
