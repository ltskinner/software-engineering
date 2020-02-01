# Logging

## Logger

* The class that actually calls the recording function
* Multiple loggers can all write to the same destination handlers

## Handler

* the `destination` for each LogRecord to be written to
  * StreamHandler
  * FileHandler
  * SMTPHandler
  * HTTPHandler

## LogRecord

* These are the actual rows logged by the loggers

## Formatters

* Specify the format of each individual record

### [Network logging](https://docs.python.org/3/howto/logging-cookbook.html)

### Errors

* Use `logging.error("message", exc_info=True)` to capture **stack trace**
* Or, if just using Exceptions
  * `logging.exception("message")` to do the same
