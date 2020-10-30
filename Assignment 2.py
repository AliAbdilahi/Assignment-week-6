prices = {
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}
stock = {"banana": 10,"apple": 0,"orange": 7,"pear": 9,}
for x in prices:
    print (x)
    print ("price: %s" % prices[x])
    print ("stock: %s" % stock[x])
total = 0
print("Prices * Stockes=")
for x in prices:
    print (prices[x] * stock[x])
    total = total + prices[x] * stock[x]

print ("Total= ", total)
