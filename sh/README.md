# .sh

## Variables

[https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-a-linux-vps](https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-a-linux-vps)

```bash
printenv
```

### Shell

```bash
SHELL_VAR='shell_var'
SHELL_VAR_NO_QUOTE=something_that_will_become_string
RESULT_OF_COMMAND="$(command)"
```

### Environment

#### Graduate SHELL Vars

```bash
export SHELL_VAR
```

#### Create New

```bash
export ENV_VAR='env_var'
```

### PATH

Add to rear

```bash
PATH=$PATH:~/opt/bin
```

Add to front

```bash
PATH=~/opt/bin:$PATH
```

### Conda (lmao)

To see env vars

```bash
conda env config vars list
```

To set new

```bash
conda activate env-name

conda env config vars set my_var=value

# be sure to reactivate it
conda activate env-name
```

## Functions

```bash
functionName() {
  echo "Echo from inside function!"
}
functionName  # call function
```

## Exit Code

```bash
python script.py

exit_code=$?  # the `$?` is some kind of magic variable

if [ "$exit_code" -eq "1" ]; then
  # 0 = Success, 1 = Failed
  echo "--> Failed fun, error caught"
fi
```
