def initCoin():
    coin = dict()
    coin["TTT"] = 0
    coin["TTH"] = 0
    coin["THT"] = 0
    coin["THH"] = 0
    coin["HTT"] = 0
    coin["HTH"] = 0
    coin["HHT"] = 0
    coin["HHH"] = 0
    return coin


for _ in range(int(input())):
    coins = list(input())
    coin = initCoin()

    for i in range(len(coins) - 2):
        coin[''.join(coins[i: i + 3])] += 1
    for i in coin.values():
        print(i, end=' ')
    print()