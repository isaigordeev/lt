
arr_ = [1,2,3,4,5,6]

def bs(arr_, el_):

    left_ = 0
    right_ = len(arr_) - 1

    while left_ <= right_:

        curr = (right_ - left_) // 2 + left_

        if arr_[curr] < el_:
            left_ = curr + 1
        elif arr_[curr] > el_:
            right_ = curr
        else:
            return curr

    
    return -1

print(bs(arr_, 3))

