file = open('file.txt', 'r+')
#
# content = file.read()
# print(content)

#
# first_line = file.readline()
# print(first_line)

all_lines = file.readlines()  # to list
print(all_lines)

file.close()



file2 = open('example.txt', 'w')
file2.write('Hello,\nWhat is your name')
file.close()

#
# file3 = open('example.txt', 'a')
# file3.write('\nMy name is professional Python.')
# file.close()


with open('example.txt', 'r') as file4:
# file4 = open('example.txt', 'r')
    content = file4.read()
print(content)
# file.close()

