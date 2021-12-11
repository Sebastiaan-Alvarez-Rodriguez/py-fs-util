import os
import setuptools
import shutil


def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    f = open(path)
    return f.read()

install_requires = [x for x in read('requirements.txt').strip().split('\n') if x]

setuptools.setup(
    name='py-fs-util',
    version='1.0.0',
    author='Sebastiaan Alvarez Rodriguez',
    author_email='a@b.c',
    description='Unix-shell like filesystem commands utility for Python',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/Sebastiaan-Alvarez-Rodriguez/py-fs-util',
    packages=setuptools.find_packages(),
    package_dir={'': '.'},
    python_requires='>=3.0',
    classifiers=(
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
    ),
    install_requires=install_requires,
)