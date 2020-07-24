items = [
    ('Product', 10),
     ('Product', 20),
      ('Product', 30),
     ]

x = list(filter(lambda item: item[1] >= 10, items))
print(x)