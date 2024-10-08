if True:
    print("This is correct indentation")

x = 5
name = "Alice"

age = 64
price = 19.95
first_name = "John"
is_online = True

if age < 18:
    print("Minor")
elif age >= 18 and age < 65:
    print("Adult")
else:
    print("Senior")

for i in range(5):
    print(i)


count = 5
while count > 0:
    print(count)
    count -= 1

def greet(name):
    return "Hello, " + name + "!"

print(greet("Alice"))


square = lambda x: x*x

print(square(4))

# List
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

print(fruits)

# tuples
coordinates = (4, 5)


print(coordinates)


# dictionary or key-value pairs -> arrays in JS
person = {
    "name": "John",
    "age": 30
          }

print(person)

# sets -> unordered collection of unique items
colors = {"red", "green", "blue"}
print(colors)

