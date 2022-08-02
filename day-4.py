import random
coin = random.randint(0,1)
print("Coin is being tossed")
if int(coin) == 0:
    print("It's head")
else:
    print("It's tails.")