letters = ["a", "b", "c"]

#add to list
letters.append("d")
print(letters)

#add to specific position
letters.insert(0, "-")
print(letters)

#to remove
letters.pop() #can pass index as well letters.pop(0)
print(letters)

#remove w/out knowing index
letters.remove("b")
print(letters)

#remove using delete can remove a range of items
del letters[0:3]

#remove all objects in list use 
letters.clear()