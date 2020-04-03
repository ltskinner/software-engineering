
class Handler(object):
    def set_successor(self, sucessor):
        pass

    def handle(self, amount):
        pass


class Dispenser(Handler):
    """ConcreteHandler"""
    def __init__(self, bill):
        self._successor = None
        self.bill = bill

    def set_successor(self, sucessor):
        self._successor = sucessor

    def handle(self, amount):
        print(self.bill, amount)
        if amount >= self.bill:
            num_bills = amount // self.bill
            print(f"Dispensing: {num_bills} - ${self.bill}")

        remainder = amount % self.bill
        if remainder != 0:
            self._successor.handle(remainder)


class ATMChain(object):
    def __init__(self):
        self.chain = []

    def add_chain(self, handle):
        if len(self.chain) > 0:
            recent = self.chain[-1]
            recent.set_successor(handle)
        self.chain.append(handle)

    def handle(self, amount):
        if self.not_whole_dollar(amount):
            raise ValueError("Please use whole dollars")

        if self.chain is None:
            raise ValueError("No handlers have been added to chain")

        entry_chain = self.chain[0]
        entry_chain.handle(amount)

    def not_whole_dollar(self, amount):
        if amount % 1 == 0:
            return False
        return True


if __name__ == "__main__":
    ATM = ATMChain()

    bills = [100, 50, 20, 10, 5, 2, 1]
    for bill in bills:
        dispenser = Dispenser(bill)
        ATM.add_chain(dispenser)

    amount = 467
    ATM.handle(amount)
