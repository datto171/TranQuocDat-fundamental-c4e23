prices = {}
prices['banana'] = 4
prices['apple'] = 2
prices['orange'] = 1.5
prices['pear'] = 3

stock = {}
stock ['banana'] = 6
stock ['apple'] = 0
stock ['orange'] = 32
stock ['pear'] = 15

total = 0
for k1, v1 in prices.items():
    for k2, v2 in stock.items():
        if k1 == k2:
            print(k1)
            print("prices", v1, sep=": ")
            print("stock", v2, sep=": ")
            print("-------")
            total += v1*v2
print(total)