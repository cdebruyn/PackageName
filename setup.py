from setuptools import setup, find_packages

setup(
    name='PackageName',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A package that uses recursion and sorting.',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/cdebruyn/PackageName',
    author='Chad',
    author_email='c.debruyn.edsa@gmail.com'
)
