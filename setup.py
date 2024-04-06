from setuptools import setup

setup(
   name='date2name',
   version='1.0',
   description='A useful module',
   author='Man Foo',
   author_email='foomail@foo.example',
   packages=['date2name'],  #same as name
   install_requires=['wheel'], #external packages as dependencies
)