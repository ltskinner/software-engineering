
"""https://realpython.com/the-most-diabolical-python-antipattern/"""

def do_something():
    print("SOMETHING")

"""Here's the punchline.

The following bit of code is one of the most destructive things a
Python developer can write:
"""
try:
    do_something()
except:
    pass
"""
Or other variants including:
except Exception:

except Exception as e:
"""

"""Why are these so bad?

They all do the sample massiver disservice: silently and invisibly
hiding error conditions that can otherwise be quickly detected and
dispatched.

Why does the author claim this to be the most "diabolical anti-pattern
in the Python world today?

    1) People do this because they expect a specific error to happen
        there. However, catching just 'Exception' hides ALL errors...
        even those which are completely unexpected
    2) When the bug is finally discovered - too often, its because it
        has shown up in production - you may have little or no idea 
        where in the code base its gone wrong. It can take you a truly
        disheartening amount of time to figure out the error is even
        happening in that try block.
    3) Once you realize the error is happening there, you are greatly
        hampered in your troubleshooting
            NO STACK TRACE
        A "literally priceless" body of information that makes the 
        difference between troubleshooting a bug in days or minutes.
    4) Bad for morale
"""

"""Bugs that arise from this negligence:

- Bugs that escape detection during development and end up in production
- Bugs that can live in production code for minutes, hors, days, or
    even weeks before realizing the bug has been happening the whole
    time
- Bugs that are hard to troubleshoot
- Bugs that are hard to fix even once you know where the supression
    exception is being raised
"""



"""The Solutions"""
def get_number():
    return int('foo')


# 1) Catch more specific exception
def basic_exception():
    try:
        do_something()
    # Catch a very specific exception - KeyError, ValueError, etc.
    except ValueError:
        pass


# 2) Log the error happened
def logger_exception():
    import logging

    try:
         get_number()
    except Exception:
        logging.exception('Caught an error')

    print("-- past --")


# 3) Log even if not using 'logging'
def traceback_exception():
    import traceback

    class ExceptionLogger:
        def log(self, text):
            pass
    
    exception_logger = ExceptionLogger()

    def log_traceback(ex):
        tb_lines = traceback.format_exception(ex.__class__, ex, 
                                              ex.__traceback__)
        tb_text = ''.join(tb_lines)
        
        exception_logger.log(tb_text)

    try:
        get_number()
    except Exception as ex:
        log_traceback(ex)


"""What You Can Do Now

1) Explicity prohibit it in your coding guidelines
2) Create (Support) Tickets for every existing 'except' in use
    -> Fix accordingly
3) Educate other team members
"""

