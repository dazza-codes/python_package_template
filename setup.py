import setuptools

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='TemplatePackageStuff',
    version='0.1.0',
    author='Darren Weber',
    author_email='dweber.consulting@gmail.com',
    packages=setuptools.find_packages(),
    scripts=[],
    url='https://test.pypi.org/project/TemplatePackageStuff/',
    license='LICENSE.txt',
    description='Useful template for package stuff.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)

