squares = [x**2 for x in range(10)]
print(squares)


# traditional way
cubes = []
for x in range(10):
    cubes.append(x**3)
print(cubes)


# conditional
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)

# nested loop
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix)
flattened = [elem for row in matrix for elem in row]
print(flattened)

# traditional nested loop
flattened = []
for row in matrix:
    for elem in row:
        flattened.append(elem)
print(flattened)

# multiple conditions
divisible_by_six = [x for x in range(100) if x % 2 == 0 if x % 3 == 0]
print(divisible_by_six)
