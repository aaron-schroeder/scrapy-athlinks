import os
from setuptools import setup


def read(rel_path):
  """Read a file so python does not have to import it.
  
  Inspired by (taken from) pip's `setup.py`.
  """
  here = os.path.abspath(os.path.dirname(__file__))
  # intentionally *not* adding an encoding option to open, See:
  #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
  with open(os.path.join(here, rel_path), 'r') as fp:
    return fp.read()


def get_version(rel_path):
  """Manually read through a file to retrieve its `__version__`.
  
  Inspired by (taken from) pip's `setup.py`.
  """
  for line in read(rel_path).splitlines():
    if line.startswith('__version__'):
      # __version__ = '0.0.1'
      delim = "'" if "'" in line else '"'
      return line.split(delim)[1]
  raise RuntimeError('Unable to find version string.')


with open('README.md') as f:
  readme = f.read()

with open('LICENSE') as f:
  license = f.read()

pkg_name = 'scrapy-athlinks'
module_name = 'scrapy_athlinks'

version = get_version(f'{module_name}/__init__.py')

setup(
  name=pkg_name,
  version=version,
  description='Web scraper for race results hosted on Athlinks.',
  long_description=readme,
  long_description_content_type='text/markdown',
  author='Aaron Schroeder',
  author_email='aaron@trailzealot.com',
  install_requires = [
    'Scrapy==2.6.2'
  ],
  # TODO: Update this
  url='https://github.com/aaron-schroeder/athlinks-scraper-scrapy',
  # project_urls={
  #   'Documentation': f'https://{pkg_name}.readthedocs.io/en/stable/',
  # },
  license='MIT',
  packages=[
    f'{module_name}',
    f'{module_name}.spiders',
    # f'{module_name}.items' # doesn't work as single-file
  ],
  classifiers=[
    'License :: OSI Approved :: MIT License',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
  ]
)