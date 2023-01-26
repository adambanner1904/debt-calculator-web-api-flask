from debt import Debt
from studentdebt import StudentDebt


class Person:

    def __init__(self, salary):
        self.salary = salary
        self.debts = {}
        self.monthly_salary = self.salary/12
        self.monthly_pay_amount = 0

    def add_debt(self, name, debt):

        # Add a debt to a list to keep track
        # of multiple debts later on
        self.debts[str(name)] = debt
        self.monthly_pay_amount = self.monthly_salary * self.debts[name].pay_percentage

    def pay_debt(self, name_of_debt):
        self.monthly_pay_amount = self.monthly_salary * self.debts[name_of_debt].pay_percentage
        # Pays back the debt a percentage of one month of the salary
        self.debts[name_of_debt].amount -= self.monthly_pay_amount

    def wipe_debt(self, name_of_debt):

        still_in_debt = True

        while still_in_debt:
            if self.monthly_pay_amount >= self.debts[name_of_debt].amount:
                self.debts[name_of_debt].months_to_wipe_out += 1
                still_in_debt = False
            else:
                self.pay_debt(name_of_debt)
                self.debts[name_of_debt].months_to_wipe_out += 1


adam = Person(40)
adam.add_debt('Student debt', StudentDebt(50))

adam.wipe_debt('Student debt')
