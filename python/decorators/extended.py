
""" https://realpython.com/primer-on-python-decorators/ """


from primer import do_twice

@do_twice
def greet(name):
    print(f"Hello {name}")

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Greetings to {name}"


if __name__ == "__main__":
    greet("bruh")

    greeting = return_greeting("breh")
    print(greeting)

