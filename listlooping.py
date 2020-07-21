letters = ["a", "b", "c"]

for letter in letters:
    print(letter)

#to get index/ it's iterable
for letter in enumerate(letters):
    print(letter)

items = [0, "a"]
index, letter = items
print(items)

for index, letter in enumerate(letters):
    print(index, letter)