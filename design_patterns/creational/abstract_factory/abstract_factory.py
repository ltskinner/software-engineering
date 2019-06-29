"""https://www.tutorialspoint.com/python_design_patterns/
python_design_patterns_abstract_factory.htm
"""

from burger_king import DoubleBacon, MTNDew, CashOnly
from macdonalds import BigMac, Coke, CreditDebit


class AbstractBurgerFactory():
    """The main focus of this is to define the interface that your Factories
    will be forced to adhere to
    """
    def get_cheeseburger(self):
        pass
    
    def get_drink(self):
        pass

    def process_payment(self):
        pass

class BurgerKingFactory(AbstractBurgerFactory):
    def get_cheeseburger(self):
        return DoubleBacon()
    
    def get_drink(self):
        return MTNDew()

    def process_payment(self):
        return CashOnly()

class MacDonaldsFactory(AbstractBurgerFactory):
    def get_cheeseburger(self):
        return BigMac()
    
    def get_drink(self):
        return Coke()

    def process_payment(self):
        return CreditDebit()

if __name__ == "__main__":

    need_bacon = True

    if need_bacon:
        burger_haus = BurgerKingFactory()
    else:
        burger_haus = MacDonaldsFactory()

    burger = burger_haus.get_cheeseburger()
    drink = burger_haus.get_drink()
    payment = burger_haus.process_payment()

    print(burger)
    print(drink)
    print(payment)
