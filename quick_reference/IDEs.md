# IDE Best Practices

## VSCode

/project
    /.vscode
        settings.json
    /project_code

### settings.json

```json
{
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.linting.pep8Enabled": true,
    "python.linting.mypyEnabled": true,
    "[markdown]": {
        "editor.tabSize": 2
    },
    "[python]": {
        "editor.rulers": [
            79
        ]
    },
    "workbench.colorCustomizations": {
        "editorRuler.foreground":"#00FFFF"
    }
}
```
