from setuptools import setup, find_packages

import os


with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


extra_files = package_files('ecldoc/Templates')
print(extra_files)
setup(
    name="ecldoc",
    version="1.0",
    packages=find_packages(),
    install_requires=['Jinja2==2.9.6', 'lxml==3.8.0'],
    package_data={'': extra_files},
    scripts=['bin/ecldoc'],
    url="https://github.com/lilyclemson/ECLDocGenerator",
    long_description=long_description,
    long_description_content_type="text/rst",
)

