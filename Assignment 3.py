groceries= ["banana","orange", "apple"]
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
def compute_bill(fruits):
    total = 0
    for x in fruits:
        if stock[item] > 0:
            total += prices[x]
            stock[item] -= 1
    return total
