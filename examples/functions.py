import sys


def diff(first, second=0):  # a is required, b is optional
    return first - second


if __name__ == '__main__':
    # Call diff with positional arguments
    result = diff(10, 2)
    print(result)

    # Call diff without specifying a value for the optional argument b
    result = diff(10)
    print(result)

    # Call diff with keyword arguments
    result = diff(second=2, first=10)
    print(result)


def varargs(*args, **kwargs):
    print(args, type(args), end=' --- ')
    print(kwargs, type(kwargs))


if __name__ == '__main__':
    varargs()
    varargs('hello')
    varargs('hello', 'world')
    varargs('hello', 'world', '!')

    varargs(name="Ana", age=20)

    varargs(1, 2, 3, name="Ana", age=20)


def all_arguments_types(a, b, *args, c, x=10, y=20, **kwargs):
    print(a, b, c, args, x, y, kwargs)


if __name__ == '__main__':
    all_arguments_types(1, 2, c=3)  # c is a required keyword-only argument


def print_clone(*values, sep=' ', end='\n', file=sys.stdout, flush=False):
    # print(type(values))
    print(*values, sep=sep, end=end, file=file, flush=flush)


if __name__ == '__main__':
    print_clone("hello", "world", sep="***")
    print_clone("hello", "world", end="***")
    print_clone('a', 'b', 'c')
