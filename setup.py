from setuptools import setup

setup(name='luizars2',
      version='0.1',
      packages=['dev_aberto'],
      author="luizars2",
      license="MIT",
      install_requires=[
          "requests",
      ],
      scripts=['scripts/hello.py']
      )