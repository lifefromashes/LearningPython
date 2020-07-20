#lists in python
letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
combined = zeros + letters
print(combined) # every object in list can be of diff type in python

numbers = list(range(20))
chars = list("Hello World")
print(numbers)
print(chars)

print(len(chars)) #to get length of items in list