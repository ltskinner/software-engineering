"""https://www.tutorialspoint.com/python_design_patterns
/python_design_patterns_factory.htm
"""


class Button(object):
    def __init__(self):
        self.html = ""

    def get_html(self):
        return self.html


class Image(Button):
    def __init__(self):
        self.html = "<img></img>"


class Input(Button):
    def __init__(self):
        self.html = "<input></input>"


class Flash(Button):
    def __init__(self):
        self.html = "<obj></obj>"


class ButtonFactory(object):
    def create_button(self, b_type):
        if b_type.upper() == 'IMAGE':
            button = Image()
        elif b_type.upper() == 'INPUT':
            button = Input()
        elif b_type.upper() == 'FLASH':
            button = Flash()
        else:
            raise ValueError(f"{b_type} is not valid button type")

        return button

if __name__ == "__main__":
    button_factory = ButtonFactory()

    buttons = ['image', 'input', 'input', 'flash', 'div']

    for b in buttons:
        new_button = button_factory.create_button(b)
        print(new_button.get_html())
