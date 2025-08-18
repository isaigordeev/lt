








# [1,1,1,2,2,2,3,3,3]
# [1,1,1,2,2,2,3,3,3]



def clean(nums):

    curr_el_count_ = 1
    prev = float("inf")
    len_ = len(nums)
    curr_spec_count_ = 0

    for i_ in range(len_-1, -len_-1, -1):
        curr_el_ = nums[i_]
        print(curr_el_, i_)
        if curr_el_ == prev:
            curr_el_count_ += 1
            print(curr_el_count_)
            if curr_el_count_ > 2:
                nums[i_+curr_el_count_-1] = -1
                curr_el_count_ -= 1
        else: 
            curr_el_count_ = 1
                
        prev = curr_el_

# [1,1,1,2,2,2,3,3,3]
####
# [1,1,-1,2,2,2,3,3,3]
######
# [1,1,2,2,-1,2,3,3,3]
########
# [1,1,2,2,-1,-1,3,3,3]
##########
# [1,1,2,2,3,-1,3,3,3]
############
# [1,1,2,2,3,3,-1,-1,-1]
#################



# [1,1,1,2,2,2,3,3,-1]
####################
# [1,1,1,2,2,3,3,-1,-1]
##################
# [1,1,2,2,-1,2,3,3,3]
####################
# [1,1,2,2,-1,-1,3,3,3]
####################
# [1,1,2,2,3,-1,3,3,3]
####################
# [1,1,2,2,3,3,-1,-1,-1]
####################


def clean_inplace(nums):


    def swap(nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    len_ = len(nums)
    edge_index_ = len_-1

    for i_ in range(len_-1, 1, -1):
        curr_el_ = nums[i_]
        edge_curr_el_ = nums[i_-2]

        if curr_el_ != edge_curr_el_:
            nums[i_] = -1
            swap(nums, i_, edge_index_)
            edge_index_ -= 1



if __name__ == "__main__":

    nums = [1,1,1,1,1,2,2,2,2,2,2,3,3]

    clean(nums)

    print(nums)



