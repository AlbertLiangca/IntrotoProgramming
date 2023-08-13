import random

def simulateCoinFlip(balance = [1000]):
    for i in range(1):
        coinResult = random.randint(1,2)
        if coinResult == 1:
            x = balance[-1]*1.5
            balance.append(x)
        elif coinResult == 2:
            x = balance[-1]*0.6
            balance.append(x)
    
    return balance[-1]

for i in range(1000):
    wallet = simulateCoinFlip()
    if wallet > 1000:
        print(wallet)
