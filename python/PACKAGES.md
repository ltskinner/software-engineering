# Packaging Relative imports

```
/package
    /subpackage
        __init__.py
        subpackage_module.py
    __init__.py
    module.py
    helper.py
```

## Import Rules

```python
# /package/module.py

# To import a module
from . import module

# To import a subpackage
from .package import package_submodule
```
