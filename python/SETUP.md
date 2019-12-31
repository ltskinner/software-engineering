# setup.py

Main components:

* README being loaded up so its displayed in PyPi
* requirements.txt being read and forced to install
* External files being bundled up with the package

```python
from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(this_directory, 'requirements.txt'), encoding='utf-8') as f:
    required = f.read().splitlines()

setup(name='spongebob',
      version='0.2.0',
      description='DeSCriPTiOn (OpTiONaL)',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/ltskinner/spongebob',
      author='ltskinner',
      license='MIT',
      install_requires=required,
      packages=['spongebob'],
      package_data={'': ['path/inside/package/spongebob.jpg', 'banner.txt']},
      zip_safe=False)
```
