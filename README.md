# ECLDoc

Ecldoc is a tool for generating API Documentation for ECL Project based on their docstrings. The executable ecldoc is the main program that parses the sources and generate Documentation.

## Requirements

- You need Python3
- Install pip3, setuptools
- Install texlive-full
- Install make

## Get started

- To install, ``cd`` to `ECLDocGenerator/`.
- Run : ``sudo make install`` (if root permissions)
- Else Run : ``make install`` (add default pip3 installation directory to $PATH env variable - most commonly $HOME/.local/bin)

Or you can install through pip:
- pip3 install https://github.com/lilyclemson/ECLDocGenerator
- pip3 install ecldoc
