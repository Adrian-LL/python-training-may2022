f = open('functions.py')  # open in read mode

for line in f:  # f is an iterator - memory efficient way of parsing file
    print(line)

f.seek(0)  # go back to the beginning of the file

file_contents = f.read()   # file contents as string

print(f.tell())  # position of cursor in file

f.seek(0)

file_lines = f.readlines()  # file contents as list of lines

f.close()


with open('functions.py') as f:
    for line in f:
        print(line)


with open('new_file', 'w') as f:
    f.write('hello\n')
    f.write('world\n')
