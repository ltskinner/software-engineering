# .sh

## Variables

[https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-a-linux-vps](https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-a-linux-vps)

```bash
printenv
```

### Shell

```bash
SHELL_VAR='shell_var'
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
