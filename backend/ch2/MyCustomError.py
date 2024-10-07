class MyCustomError(Exception):
    pass
try:
    raise MyCustomError("An error occurred")
except MyCustomError as e:
    print(e)
    