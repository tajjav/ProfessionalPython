num_string = "10"

print(num_string)
print(type(num_string))
num = int(num_string)


print(num)
print(type(num))


# control structures
x = 5
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

y = 11
if y > 10:
    print("y is greater than 10")
elif y == 10:
    print("y is exactly 10")
else:
    print("y is not greater than 10")


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for x in range(10):
    print(x)

# while loop
x = 0
while x < 5:
    print(x)
    x += 1

# iterating over sequence
person = {"name": "John", "age": 30}
for key, value in person.items():
    print(f"{key}: {value}")


for x in range(5):
    if x == 3:
        continue
    print("x :", x)

'''
for y in range(5):
    if y == 3:
        continue
        print("y :", y)
'''

for z in range(3):
    if z == 2:
        break
    print(z)
else:
    print("Finished looping")

