
""" https://realpython.com/primer-on-python-decorators/ """


from simple_examples import debug, timer
from primer import do_twice


""" Decorate class internally """
class TimeWaster:
    @debug
    def __init__(self, max_num):
        self.max_num = max_num
    
    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])


""" Debug doing it twice """
@debug
@do_twice
def debug_do_twice_greet(name):
    print(f"Hello {name}")

""" Debug twice """
@do_twice
@debug
def debug_twice_greet(name):
    print(f"Hello {name}")

if __name__ == "__main__":
    tw = TimeWaster(1000)
    tw.waste_time(999)

    debug_do_twice_greet("bru")

    debug_twice_greet("urb")


