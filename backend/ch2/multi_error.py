try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ZeroDivisionError:
    print("You cannot divide by Zero!")
except ValueError:
    print("Please enter a valid integer.")
else:
    print("division is performed!")



try:
    print("Trying to open the file...")
    file = open('file.txt', 'r')
except FileNotFoundError:
    print("File not found.")
#else:
 #   print("File opened successfully.")
  #  file.close()

finally:
    print("This block executes no matter what.")
    try:
        file.close()
    except NameError:
        print("file not found to close")



if x < 0:
    raise ValueError("x must be non negative")