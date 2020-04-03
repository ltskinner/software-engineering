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
