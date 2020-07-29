# YAML Reading

```python
import os
import yaml

print(os.environ['DEV_TEST_PROD'])

with open("yaml_file.yaml", 'r') as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)


print(config)
```
