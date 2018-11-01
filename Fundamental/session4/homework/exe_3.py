prices = {}
prices['banana'] = 4
prices['apple'] = 2
prices['orange'] = 1.5
prices['pear'] = 3
print(prices)

stock  = {}
stock['banana'] = 6
stock['apple'] = 0
stock['orange'] = 32
stock['pear'] = 15
print(stock)

for i in range(len(prices)):
    if i == 0:
        for x in prices.keys():
            print(x)

        for a in prices.values():
            print("prices", a, sep=": ")

        for b in stock.values():
            print("stock", b, sep=": ")