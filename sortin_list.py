numbers = [3, 52, 2, 6, 8]

numbers.sort()
print(numbers)

#sort in reverse
numbers.sort(reverse=True)
print(numbers)

numbers2 = [4, 2, 5, 1]
print(sorted(numbers2)) # returns new list that is sorted. Doesnt modify original

#sort items in tuple
items = [
    ("Product", 10),
    ("Product", 9),
    ("Product", 12),
]

def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)
