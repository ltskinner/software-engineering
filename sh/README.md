# .sh

## Shell Variables

```sh
SHELL_VAR='shell_var'
SHELL_VAR_NO_QUOTE=something_that_will_become_string
RESULT_OF_COMMAND="$(command)"

echo "SHELL_VAR: '$SHELL_VAR'"  # note dont use `` cause those are interpreted literally
```

### Env Var Upgrade

```sh
# Upgrade existing SHELL var
export SHELL_VAR

# Create new Env var directly
export ENV_VAR='env_var'
```

### Add to PATH

```sh
# Add to REAR
PATH=$PATH:~/opt/bin

#Add to FRONT
PATH=~/opt/bin:$PATH
```

### See All Vars

[https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-a-linux-vps](https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-a-linux-vps)

```bash
printenv
```

### Conda Vars

```sh
# See env vars
conda env config vars list

# To set new
conda activate env-name
conda env config vars set my_var=value

# Reactivate to take effect
conda activate env-name
```

## Conditional Logic

### Capturing Exit Codes

```bash
python deliberate_fail.py

EXIT_CODE=$?  # the `$?` is some kind of magic variable

SUCCEEDED="0"
FAILED="1"

if [ "$EXIT_CODE" -eq $FAILED ]; then
  echo "--> Failed fun, error caught"
fi
```

### Other Evaluation Methods

```sh
# ./script.sh "expected_1"

if [ $1 = "expected_1" ]; then
    echo "Expected condition: '$1'"
elif [ $1 = "expected_2" ]; then
    echo "Expected condition 2: '$2'"
else
    echo "No expected conditions - exiting"
    exit 1
fi
```

## Functions

```sh
functionName() {
  echo "Echo from inside function!"
}
functionName  # call function
```

### Parameters

```sh
# ./script.sh "cli_param"

functionWithParams() {
  # note - these are positional args local to the function call
  #      - the `$1` arg passed in is only at [1] in the scope of the caller execution

  echo "param1: '$1'"
  echo "param2: '$2'"
  echo "param3: '$3'"
}

functionWithParams "param1" 2 $1

# Output:
# param1: 'param1'
# param2: '2'
# param3: 'cli_param'
```
