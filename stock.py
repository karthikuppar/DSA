def maxProfit(arr):
    min_price = arr[0]
    max_profit = 0

    for price in arr:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)

    return max_profit