c = 20

if c > 10:
    print('yes!')
    print('still under if')
elif c > 0:
    print('Over 0')

print('outside if')

print('while output:')
while c > 10:
    print(f'c = {c}')
    print('Doing more stuff ...')
    c -= 2  # c = c - 2

print('for output (iterate on string):')
greeting = 'hello'  # strings are iterable
for character in greeting:
    print(character)

print('for output (iterate on range of numbers):')
for i in range(1, 10, 2):
    print(i)

x = 0
while True:
    print(x)
    x += 1
    if x == 5:
        break


while x < 10:
    x += 1
    if x % 2 == 0:
        continue
    print(x)
