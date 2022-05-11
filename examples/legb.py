# Global
x = 100


def func(a):
    b = 10

    def inner(c):
        d = 1

        print('Local names (inside inner):', c, d)
        print('Enclosing names (inside inner):', a, b)
        print('Global names (inside inner):', x, func)
        print('Built-in names (inside inner):', len, list, ValueError)

    inner(2)

    print('Local names (inside func):', a, b, inner)
    print('Global names (inside func):', x, func)
    print('Built-in names (inside func):', len, list, ValueError)


func(20)

print('Built-in names:', len, list, ValueError)
print('Global names:', x, func)
