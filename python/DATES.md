# Dates in Python

```python
from datetime import datetime, timedelta

# Now
now_time = datetime.now()
print(f'datetime.now(): {now_time}')

# datetime to string
str_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
print(f'strftime: {str_time}')

# datetime from string
dt_obj = datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')
print(f'strptime: {dt_obj}')

# Time difference
time_diff = timedelta(
    days=31,
    seconds=45,
    microseconds=20,
    milliseconds=23,
    minutes=5,
    hours=8,
    weeks=2
)
print(f'time_diff: {time_diff}')

delta = datetime.now() - time_diff
print(f'delta: {delta}')
```

## Resources

* [Other formatting options](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)
* [Cleaner representation](https://www.w3schools.com/python/python_datetime.asp)
