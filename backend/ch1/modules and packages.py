import math, my_module as my
print(math.sqrt(16))

print(my.cube(3))


try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot play with zero in denominator")