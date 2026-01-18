def StockBuyAndSell(arr):
    min_price=float('inf')
    max_profit=0
    for price in arr:
        if price<min_price:
            min_price=price
        profit=price-min_price
        max_profit=max(max_profit,profit)
    return max_profit
arr=[8, 6, 4, 3, 1]
print(StockBuyAndSell(arr))
