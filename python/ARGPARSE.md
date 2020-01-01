
# argparse

```python
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--some_int', action='store',
                       type=int, required=True, default=42)
args = my_parser.parse_args()
print(args.some_int)


my_parser.add_argument('--some_str', action='store', type=str, required=True)
my_parser.add_argument('--some_bool', action='store_ture', type=bool, required=True)
my_parser.add_argument('--id', action='store', type=int)

my_parser.add_argument('-default', action='store', default='default_value')

my_parser.add_argument('-limited_options', action='store', choices=['head', 'tail'])
my_parser.add_argument('-range_options', action='store', choices=range(1, 10))

#   const=  overrides specified value
# default=  exists if no value given
my_parser.add_argument('-store', action='store')
my_parser.add_argument('-store_predef_constant', action='store_const', const=42)
my_parser.add_argument('-store_true', action='store_true')
my_parser.add_argument('-store_false', action='store_false')
my_parser.add_argument('-list_append', action='append')
my_parser.add_argument('-list_append_predef_constant', action='append_const', const=42)
my_parser.add_argument('-count_num_option_appearances', action='count')
my_parser.add_argument('-help', action='help')
my_parser.add_argument('-version', action='version')

args = my_parser.parse_args()

print(args.some_int)
```
