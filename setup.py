from setuptools import setup
from setuptools import find_packages

setup(
    name='my_ns.pkg1',
    version='0.1.0',
    author="Laurent LAPORTE",
    author_email="tantale.solutions@gmail.com",
    url="https://github.com/tantale/namespace-packages-demo",
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    namespace_packages=['my_ns'],
)
