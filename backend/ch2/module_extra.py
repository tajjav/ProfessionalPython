from functions import add_numbers
# from package import submodule1, submodule2
from package.submodule1 import foo
from package.submodule2 import bar

result_number = add_numbers(11, 10)
print(result_number)

#submodule1.foo()
#submodule2.bar()

foo()
bar()
