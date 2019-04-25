
"""https://docs.python-guide.org/writing/tests/"""


"""Testing code is important

Getting used to writing testing code and running it in parallel is
considered a good habit.

Some general rules:
- A testing unit should focus on one tiny bit of functionality and 
    prove it correct
- Each test must be fully independant
    - run alone
    - run in any order
    - may need to be handled by setUp() and tearDown() methods
- Tests must run fast, if they are slow, people wont use them and they
    will slow down development
    - heavy tests can be run in a scheduled suite
- Learn your tools and learn how to run a single test or test case. When
    developing a function inside a module, run this functions tests
    frequently. Ideally automatically when you save the code
- Always run the full test suite before a coding session, and run it 
    again after. This will give you more confidence that you did not
    break anything in the rest of the code.
- It is a good idea to implement a hook that runs all tests before
    pushing code to a shared repo
- If you are in the middle of a development session and have to 
    interrupt your work, it is a good idea to write a broken unit test
    about what you want to develop next. When coming back to work there
    will be a pointer of where to get back to work
"""

