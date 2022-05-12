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
            raise ValueError('Operation not allowed')
        self.balance -= amount


if __name__ == '__main__':
    ba = BankAccount("ING", 1000)
    print(ba.bank_name, ba.balance)

    ba.deposit(100)
    print(ba.balance)

    ba.withdraw(500)
    print(ba.balance)

    ba.withdraw(700)
    print(ba.balance)

