
with open('ctx.py') as f:
    pass

# some setup action
# some teardown action
# want to combine the two

from sqlite3 import connect 

with connect('test.db') as conn:
    cur = conn.cursor()
    cur.execute('create table points(x int, y int)')
    cur.execute('insert into points (x, y) values (1, 1)')
    cur.execute('insert into points (x, y) values (1, 2)')
    cur.execute('insert into points (x, y) values (2, 1)')
    for row in cur.execute('select x, y from points'):
        print(row)
    for row in cur.execute('select sum(x + y) from points'):
        print(row)
    cur.execute('drop table points')


"""
class temptable:
    def __init__(self, cur):
        self.cur = cur
    def __enter__(self):
        print("__enter__")
        self.cur.execute('create table points(x int, y int)')
    def __exit__(self, *args):
        print("__exit__")
        self.cur.execute('drop table points')

with connect('test.db') as conn:
    cur = conn.cursor()
    with temptable(cur):
        cur.execute('insert into points (x, y) values (1, 1)')
        cur.execute('insert into points (x, y) values (1, 2)')
        cur.execute('insert into points (x, y) values (2, 1)')
        for row in cur.execute('select x, y from points'):
            print(row)
        for row in cur.execute('select sum(x + y) from points'):
            print(row)
"""
"""
def temptable(cur):
    cur.execute('create table points(x int, y int)')
    yield
    cur.execute('drop table points')

class contextmanager:
    def __init__(self, cur):
        self.cur = cur
    def __enter__(self):
        self.gen = temptable(self.cur)
        next(self.gen)
    def __exit__(self, *args):
        next(self.gen, None)

with connect('test.db') as conn:
    cur = conn.cursor()
    with contextmanager(cur):
        cur.execute('insert into points (x, y) values (1, 1)')
        cur.execute('insert into points (x, y) values (1, 2)')
        cur.execute('insert into points (x, y) values (2, 1)')
        for row in cur.execute('select x, y from points'):
            print(row)
        for row in cur.execute('select sum(x + y) from points'):
            print(row)

"""

# All this is already in context lib
from contextlib import contextmanager
class contextmanager_local:
    def __init__(self, gen):
        self.gen = gen
    def __call__(self, *args, **kwargs):
        # Do this to capture params
        self.args, self.kwargs = args, kwargs
        return self
    def __enter__(self):
        self.gen_inst = self.gen(*self.args, **self.kwargs)
        next(self.gen_inst)
    def __exit__(self, *args):
        next(self.gen_inst, None)

# Decorate baby
@contextmanager
def temptable(cur):
    cur.execute('create table points(x int, y int)')
    try:
        yield
    finally:
        cur.execute('drop table points')

# Original
#temptable = contextmanager(temptable)


with connect('test.db') as conn:
    cur = conn.cursor()
    #with contextmanager(temptable)(cur):
    with temptable(cur):
        cur.execute('insert into points (x, y) values (1, 1)')
        cur.execute('insert into points (x, y) values (1, 2)')
        cur.execute('insert into points (x, y) values (2, 1)')
        for row in cur.execute('select x, y from points'):
            print(row)
        for row in cur.execute('select sum(x + y) from points'):
            print(row)