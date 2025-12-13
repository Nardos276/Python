"""prices=[120, 45, 300, 85, 150]
def get_expensive_products():
    Expensive_prices=[]
    for i in range (len(prices)):
        if prices[i] > 100:
            Expensive_prices.append(prices[i])
        else:
            continue
    return Expensive_prices
print(get_expensive_products())"""
"""prices= [120, 45, 300, 85, 150]
expensive=[]
for i in range (len(prices)):
    if prices[i] > 100:
        expensive.append(prices[i])
    else:
        continue
print(expensive)"""
with open("log.txt", "a") as file:
    file.write("User logged in\n")
with open("log.txt", "r") as file:
    log_history= file.read()
print(log_history)



