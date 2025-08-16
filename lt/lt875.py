

# piles = [2, 3, 5, 6] # h = 8
piles = [3,6,7,11]
h = 8

def koko(piles, h):
    min_ = min(piles)
    max_ = max(piles)

    for k in range(min_, max_+1):
        curr_h = h

        for pile in piles:
            curr_h -= ( (pile+k-1)//k ) 
            if curr_h <= 0:
                break

        if curr_h < 0:
            continue
        else: 
            return k

def koko_bin(piles, h):
    min_k = 1
    max_k = max(piles)

    while min_k < max_k:
        curr_k = ( max_k - min_k ) // 2 + min_k
        curr_h = h

        for pile in piles:
            curr_h -= ( (pile+curr_k-1)//curr_k ) 
            if curr_h < 0:
                break

        if curr_h < 0:
            min_k = curr_k + 1
        elif curr_h >= 0:
            max_k = curr_k


    return min_k

        
print(koko_bin(piles, h))
