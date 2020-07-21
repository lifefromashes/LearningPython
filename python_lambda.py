items = [
    ("Product", 10),
    ("Product", 9),
    ("Product", 12),
]

#def sort_item(item):
    #return item[1]

items.sort(key=lambda item:item[1])
print(items)
