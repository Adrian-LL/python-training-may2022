print('hello world')
print('hello!')

command = "/Users/iulia/.virtualenvs/python-training-may2022/bin/python "\
          "/Users/iulia/PycharmProjects/python-training-may2022/examples/"\
          "script.py"

command_2 = ("/Users/iulia/.virtualenvs/python-training-may2022/bin/python "
             "/Users/iulia/PycharmProjects/python-training-may2022/examples/"
             "script.py")

multiline_string = """
/Users/iulia/.virtualenvs/

python-training-may2022/bin/python 
/Users/iulia/PycharmProjects/
python-training-may2022/examples/script.py
"""

print(command)

print(multiline_string)

a = 10
b = 12

c = b / a

print(c, type(c))

print("\nSimple quote: \'\nDouble quote: \"\nBackslash: \\")
