numbers = [1, 2, 3]
first = numbers[0]
second = numbers[1]
third = numbers[2]

#listUnpacking
numbers = [1, 2, 3]

first, second, third = numbers #num variables have to be same as whats in list
numbers = [1, 2, 3, 4, 4, 4, 4]

first, second, *other = numbers #gets first and second and stores rest in another list
print(first)
print(other)

#first and last item
first, *other, last = numbers
print(first, last)
print(other)