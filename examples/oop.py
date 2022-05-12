# class == type -> pattern / rețetă -> general
# instance == object -> instanță -> concret
# method -> function defined inside a class

class Person:
    count = 0  # class attribute

    def __init__(self, name, age=None):
        self.name = name  # instance attribute
        self.age = age
        Person.count += 1

    def say(self, greeting):  # instance method
        print(f'{self.name} says "{greeting}"')


if __name__ == '__main__':
    print('Person count:', Person.count)

    x = Person('Ana', 10)
    print('Value for attribute name outside of object x:', x.name)
    x.say('Hello')

    print('Person count:', Person.count)

    y = Person('Marian')
    y.say('Hi')

    print('Person count:', Person.count)
