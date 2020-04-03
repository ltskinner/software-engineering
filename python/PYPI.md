# PyPi Distribution Sequence

[https://packaging.python.org/tutorials/packaging-projects/](https://packaging.python.org/tutorials/packaging-projects/)

## Builds whatever version is in:

**Be sure to update `setup.py` with the new version before you build**

```bash
python setup.py sdist bdist_wheel
```

## Distributes it --> version = {0.1.1}

**Distros will be in `/dist` at the same level as `setup.py`**

```bash
python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*{version}*
```
