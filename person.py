
class Person:

    def __int__(self, salary):
        self.salary = salary
        self.debts = {}

    def add_debt(self, name, debt):

        self.debts[str(name)] = debt

    def pay_debt(self, name):
        pass

    def wipe_debt(self):
        pass


