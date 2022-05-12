from datetime import date

# class == type -> pattern / rețetă -> general
# instance == object -> instanță -> concret
# method -> function defined inside a class


class Person:
    count = 0  # class attribute

    def __init__(self, name, date_of_birth=None):
        self.name = name  # instance attribute
        self.date_of_birth = date_of_birth
        self.increment_count()

    def say(self, greeting):  # instance method
        print(f'{self.name} says "{greeting}"')

    @property
    def age(self):
        diff = date.today() - self.date_of_birth
        return diff.days // 365

    @classmethod
    def increment_count(cls):
        cls.count += 1

    def __lt__(self, other):
        if self.date_of_birth > other.date_of_birth:
            return True
        return False

    def __str__(self):
        return f'Name is {self.name}; Age is {self.age}'


class Student(Person):
    def __init__(self, *args, **kwargs):
        self.university = kwargs.pop('university', None)
        super().__init__(*args, **kwargs)

    def __str__(self):  # overwrite method from parent
        return f'Student {self.name} at {self.university}'

    @staticmethod
    def has_scholarship(self):  # add extra method
        return True


if __name__ == '__main__':
    print('Person count:', Person.count)

    x = Person('Ana', date(2012, 2, 3))
    print('Value for attribute name outside of object x:', x.name)
    x.say('Hello')

    print('Person count:', Person.count)

    y = Person('Marian', date(2002, 5, 12))
    y.say('Hi')
    print(f"{y.name}'s age is {y.age}")

    print('Person count:', Person.count)

    print(x < y)  # x.__lt__(y)
    print(y < x)  # y.__lt__(x)

    print(x)

    Person.increment_count()

    print(x.name)  # get
    x.name = 'Andreea'  # set
    del x.name  # delete

    s = Student('Dana', date(1997, 2, 3), university="Poli")
    print(s)
    s.say("Bună")
