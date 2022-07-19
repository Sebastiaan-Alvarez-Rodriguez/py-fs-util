# py-fs-util
Unix-shell like filesystem commands utility for Python

## Goal
The goal of this project is to make filesystem-like commands available in Python,
such that UNIX shell users can interact **intuitively** with the filesystem.
E.g, the following commands must be supported:
```python
mkdir('/tmp/foo')
ls('/tmp')
touch('/tmp/foo/bar.hi_there')
ln('/tmp/foo','/tmp/just_a_link')
rm('/tmp/foo')
```

## Requirements
The only requirement for running:
    + python `3.0+`

For installation using pip, requires:
    + `setuptools>=24.2.0`


## Compatibility
This project should be compatible with Python `3.0+`.
From personal experience, we know this project operates with Python `3.2` up to (including) `3.9`.
 > Should you find a bug, create a new issue, noting (1) the command, (2) the input, (3) the output, and (4) the Python version. 


## Installation
There are 2 ways to install and use this project.
 1. Install the package using pip: Open a terminal insidede the root of the cloned repository, and type `pip3 install .`
 2. place `py_fs_util` in your project and use it from there.


## Usage
The original authors intended use of the software like this:
```python
import py_fs_util as fs

# print only the files (not directories, symlinks, special socket files)
for path in fs.ls('/tmp', only_files=True):
    print(path)
fs.mkdir('/tmp/some/dirs')
fs.touch('/tmp/some/file.ext')

# deliver paths as full (absolute) paths.
for path in fs.ls('/tmp/some', full_paths=True):
    print(path)

fs.cp('/tmp/some', '/tmp/other')
```



## Supported commands
The following pure-UNIX commands are supported:
```bash
cp
ln
ls
mkdir
mv
rm
touch
```

Besides these functions, we also provide utility functions:
```python
abspath(path)                         # Absolute path for given path
abspathfile(path)                     # Absolute path for a given file
basename(path)                        # Base filename (/tmp/a.b --> a.b)
cwd()                                 # Current Work Directory
dirname(path)                         # Dir filename (/tmp/a.b --> /tmp)
exists(path, args)                    # Check whether given path exists
isdir(path, args)                     # Check whether given path is a directory
isemptydir(path, args)                # Check whether given dir is empty
isfile(path, args)                    # Check whether given path is a file
issymlink(path, args)                 # Check whether given path is a symlink
resolvelink(path, args, full_resolve) # Resolves a link to its target
join(path, args)                      # Joins multiple parts together as a path
sep()                                 # Path separator for current platform
sizeof(path)                          # Size of given file
split(path)                           # Splits path based on sep()
relpath(path, start)                  # Relative filepath to path from start
unpack(filename, extract_dir)         # Unpacks given file (.zip/.tar/.tar.xz...) to given extract_dir
```