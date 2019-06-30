
from meals import Sandwich, Burrito, Salad


class Command(object):
    def execute(self):
        pass


class SandwichCommand(Command):
    """ConcreteCommand"""
    def __init__(self, sandwich: Sandwich):
        self._sandwich = sandwich

    def execute(self):
        self._sandwich.make_sammy()


class BurritoCommand(Command):
    """ConcreteCommand"""
    def __init__(self, burrito: Burrito):
        self._burrito = burrito

    def execute(self):
        self._burrito.make_burrito()


class SaladCommand(Command):
    """ConcreteCommand"""
    def __init__(self, salad: Salad):
        self._salad = salad

    def execute(self):
        self._salad.make_salad()


class MealInvoker(object):
    """Invoker"""
    def __init__(self):
        self._command = None
        self._command_list = list()

    def set_command(self, command: Command):
        self._command = command

    def add_command_to_list(self, command: Command):
        self._command_list.append(command)

    def execute_commands(self):
        for cmd in self._command_list:
            cmd.execute()

        self._command_list.clear()

    def invoke(self):
        if self._command is None:
            raise ValueError("use set_command() to set a command")
        self._command.execute()


if __name__ == "__main__":

    sandwich = Sandwich()  # receiver
    command_sandwich = SandwichCommand(sandwich)  # concrete command

    burrito = Burrito()
    command_burrito = BurritoCommand(burrito)

    meal = MealInvoker()
    meal.set_command(command_sandwich)

    meal.invoke()

    meal.add_command_to_list(command_sandwich)
    meal.add_command_to_list(command_burrito)
    meal.execute_commands()

    
