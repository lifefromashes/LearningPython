def greet():
    print("Hi there")
    print("welcome aboard")


greet()


def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("welcome aboard")


greet("Kristin", "Skipper")

def greet(name):
    print(f"Hi {name}")

#return a value instead of print
def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Kristin")

print(message)

def increment(number, by):
    return number + by

result = increment(2, 1)
print(result)

print(increment(2, 1))
