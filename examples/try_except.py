name = input("What's your name? ")
print(len(name))

try:
    if not name[0].isalpha():
        raise ValueError('Invalid name')

    print(f'Hello, {name}! You are in drawer {name[0]}!')
except IndexError as ex:
    print(f'Error occurred: {ex}')
except TimeoutError:
    print('Doing something different')
else:
    print('... searching patient file')
finally:
    print('Executes every time')
