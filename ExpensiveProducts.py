prices=[120, 45, 300, 85, 150]
def get_expensive_products():
    Expensive_prices=[]
    for i in range (len(prices)):
        if prices[i] > 100:
            Expensive_prices.append(prices[i])
        else:
            continue
    return Expensive_prices
print(get_expensive_products())

