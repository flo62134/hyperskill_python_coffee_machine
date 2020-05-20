class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.cents += deposit_cents
        self.dollars += deposit_dollars
        self.extra_cents_to_dollars()

    def extra_cents_to_dollars(self):
        if self.cents >= 100:
            extra_dollars = self.cents // 100
            self.dollars += extra_dollars
            self.cents -= extra_dollars * 100
