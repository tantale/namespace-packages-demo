NOTICE
======

The `my_ns` directory is a **namespace package**.

Normally, since Python 3.3 and [PEP 420 — Implicit Namespace Packages](https://www.python.org/dev/peps/pep-0420/), this directory should not contains an `__init__.py`.

We are using [setuptools](https://setuptools.readthedocs.io) for packaging.
Currently, there is an issue with the function `find_packages()`, used to discover Python packages in source code: [find_packages() doesn't find PEP 420 packages](https://github.com/pypa/setuptools/issues/97).

So, the best way fix that is to use the old way: add a `__init__.py` file with the following content:

    try:
        import pkg_resources
    
        pkg_resources.declare_namespace(__name__)
    
    except ImportError:
        from pkgutil import extend_path
    
        __path__ = extend_path(__path__, __name__)
