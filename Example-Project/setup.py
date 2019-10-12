from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(this_directory, 'requirements.txt'), encoding='utf-8') as f:
    required = f.read().splitlines()

setup(name='example_project',
      version='0.0.0',
      description='Example project file structure',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/ltskinner/software-engineering',
      author='ltskinner',
      license='MIT',
      install_requires=required,
      packages=['example_project'],
      package_data={'': ['lib/banner.txt']},
      zip_safe=False)
