import heapq

coins = [1, 2, 5]
target = 11

# greedy approach fails here
def amount(coins, target):
    neg_coins = [coin * -1 for coin in coins]
    heapq.heapify(neg_coins)

    num_coins = 0
    while target != 0:
        curr_coin = heapq.heappop(neg_coins) * -1
        curr_num = target // curr_coin
        if curr_num > 0:
            num_coins += curr_num
            target -= curr_num * curr_coin
            if target < 0:
                return -1
        else:
            continue

    if target == 0:
        return num_coins
    else:
        return -1


# table[i+1] = min(table[i], (i + 1) // coin, table[i])
# table[i+1] = min(table[i-j] + table[1+j]) for all j

# # 0 1 2 3 4 5 6 7 8 9 10 11
# # 0 - - - - - - - - - - -
# 1 - 1 2 3 4 5 6 8 8 9 10 11
# 4 -
# 5 -


# din programming
def din_amount(coins, target):
    min_table = [int(float('inf'))] * len(target+1)
    min_table[0] = 0

    for coin in coins:
        for i in range(1, target+1):
            if i - coin >= 0:
                min_table[i] = min(min_table[i], min_table[i - coin] + 1)

        return min_table[target] if min_table[target] != int(float('inf')) else -1


def stupid_din_amount(coins, target):
    min_table = [float('inf')] * (target+1)
    min_table[0] = 0

    for coin in coins:
        min_table[coin] = 1

    def traverse(table, i, target):
        if i > target:
            return float('inf')
        return min(min_table[target] + min_table[i], traverse(table, i + 1, target-1))

    for i in range(1, target+1):
         min_table[i] = traverse(min_table, 0, i)

if __name__ == '__main__':
    print(stupid_din_amount(coins, target))




