letters = ["a", "b", "c", "d"]

letters[0] = "A"

print(letters)

print(letters[0:3]) # return new list w/first 3 items
print(letters[:3])
print(letters[0:])# returns all items in original list
#pass a step when want to return every 2nd or 3rd ele in list
print(letters[::2])

numbers = list(range(20))
print(numbers[::2])
print(numbers[::-1])