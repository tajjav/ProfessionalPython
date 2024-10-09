def my_decorator(func):
  def wrapper(*args, **kwargs):
    print("Something is happening before the function is called")
    result = func(*args, **kwargs)
    print("Something is happening after the function is called")
    return result
  return wrapper


def say_hello():
  print("Hello!")


say_hello = my_decorator(say_hello)
say_hello()

# above code is same as below
@my_decorator
def say_hell():
  print("Hello!")


# decorator with arguments
@my_decorator
def say_hello(name):
  print(f"Hello {name}!")