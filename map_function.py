items = [
    ("Product", 10),
    ("Product", 9),
    ("Product", 12),
]

#prices = []
#for item in items:
    #x = prices.append(item[1])

x = map(lambda item: item[1], items)
for item in x:
    print(item)

prices = list(map(lambda item: item[1], items))
print(prices)

 