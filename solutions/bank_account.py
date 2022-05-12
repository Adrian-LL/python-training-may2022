class InsufficientFunds(Exception):
    pass


class BankAccount:
    """
    This class describes the behaviour of a bank account
    Users can withdraw and deposit money
    """
    def __init__(self, bank_name: str, balance: int):
        """
        :param bank_name: name of the bank
        :param balance: available money
        """
        self.bank_name = bank_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFunds('Operation not allowed')
        self.balance -= amount


class Employee:
    def __init__(self, name: str, bank_account: BankAccount, salary: int = 0):
        self.name = name
        self.bank_account = bank_account
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    def raise_salary(self, percent):
        if percent not in (5, 10, 20):
            raise ValueError('Invalid percent')
        self._salary += percent / 100 * self._salary

    def receive_salary(self):
        # self.bank_account.balance += self.salary
        self.bank_account.deposit(self._salary)


if __name__ == '__main__':
    ba = BankAccount("ING", 1000)
    # print(ba.bank_name, ba.balance)
    #
    # ba.deposit(100)
    # print(ba.balance)
    #
    # ba.withdraw(500)
    # print(ba.balance)

    emp = Employee('Ana Popescu', ba, 100)
    emp.raise_salary(5)
    emp.receive_salary()
    print(emp.name, emp.salary, emp.bank_account.balance)
    print(vars(emp))
    print(vars(emp.bank_account))

    try:
        emp.salary = 1000
    except AttributeError as ex:
        print(ex)

    emp2 = Employee('Mihai Ionescu', BankAccount("BCR", 2000))

