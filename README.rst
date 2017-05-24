Namespace package demo
======================

This project is a short demonstration of namespace package in Python.

The source code is as follow:

    ==========================  =================================================
    setup.py                    Has the property ``namespace_packages=['my_ns']``
    src/my_ns/__init__.py       Old way to declare a namespace package       
    src/my_ns/pkg1/__init__.py  Classic package ``my_ns.pkg1``
    src/my_ns/pkg1/foo.py       Classic module ``my_ns.pkg1.foo``
    ==========================  =================================================
