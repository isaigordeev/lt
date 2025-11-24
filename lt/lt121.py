# LeetCode 121 - Best Time to Buy and Sell Stock (Easy)
#
# Дан массив prices где prices[i] - цена акции в i-й день.
# Максимизируй прибыль, выбрав один день для покупки и другой день в будущем для продажи.
# Верни максимальную прибыль. Если прибыль невозможна, верни 0.
#
# Пример 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Объяснение: Купи в день 2 (цена = 1) и продай в день 5 (цена = 6), прибыль = 6-1 = 5.
#
# Пример 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Объяснение: Нет транзакции, прибыль = 0.
#
# Constraints:
# - 1 <= prices.length <= 10^5
# - 0 <= prices[i] <= 10^4

# [7,1,5,3,6,4]
# [7,1,5,3,6,4]

#  F_i = f(i+1) - f(i)
#  P_0 = F_0
#  P_(i+1) = max(P_i, P_i+f(i+1)-f(i), P_i+f(i+1)-f(i))


def maxProfit(prices) -> int:
    if not prices or len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        # Calculate profit if we sell today
        profit = prices[i] - min_price
        max_profit = max(max_profit, profit)

        # Update minimum price if today's price is lower
        min_price = min(min_price, prices[i])

    return max_profit
