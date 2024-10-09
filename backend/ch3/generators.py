# generator
def my_generator():
  yield 1
  yield 2
  yield 3


gen = my_generator()

for value in gen:
  print(value)
  




# generator expression
gen_expr = (x**2 for x in range(10))
for value in gen_expr:
  print(value)




