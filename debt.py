
class Debt:

    def __init__(self, amount, pay_percentage, interest_rate):

        self.amount = amount
        self.pay_percentage = pay_percentage
        self.months_to_wipe_out = 0
        self.interest_rate