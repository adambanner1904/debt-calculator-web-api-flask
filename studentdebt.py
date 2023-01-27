from debt import Debt


class StudentDebt(Debt):

    def __init__(self, amount, pay_percentage=0.09, interest_rate=0.03):
        Debt.__init__(self, amount, pay_percentage)
        self.pay_threshold = 27295
