# Git Usage

[Version control overview](./OVERVIEW.md)

## Better Usage

```bash
$ git checkout branch_name
*make edits*
$ git add *fname*
$ git commit -m "edited file"
$ git push
*merge in browser*
$ git checkout master
$ git fetch
$ git merge branch_name
```

## Basic Usage

```bash
$ git status
$ git add folder/*
$ git add folder/file.md
$ git commit -m "commit message"
$ git pull
$ git push
```

### Undoing Commits

```bash
# Undo and save changed locally
$ git reset --soft HEAD~1

# Undo and delete local changes
$ git reset --hard HEAD~1
```

## Branches

```bash
# Creating a new branch
$ git checkout -b <branch_name>

# Initial push = after this, can use regular push
# -u stands for `upstream`
$ git push -u origin <branch_name>

# Switch back to master
$ git checkout master

# Merge with master
$ git merge <branch_name>
$ git push

# Delete local branch
$ git branch -d <branch_name>

# Delete remote branch
$ git push origin --delete <branch_name>
```

### Misc branch usage

```bash
# Compare branches
$ git show-branch <branch_name> master

# checkout old state to monkey around with - cant make commits tho
$ git checkout <SHA>
```

## Initializing a repo from a local folder

```bash
$ mkdir example-repo
$ cd example-repo
$ git init
```

## Misc

```bash
# Exit `log` or `diff`
$ q
```
