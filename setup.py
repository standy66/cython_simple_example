from setuptools import setup, find_packages
from setuptools.extension import Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        "my_package.math",
        ["my_package/math.pyx"],
        libraries=["m"],
    ),
    Extension(
        "my_package.lib",
        ["my_package/lib.pyx"],
    ),
]

print(find_packages())

setup(
    name="my_package",
    packages=["my_package"],
    ext_modules=cythonize(extensions),
    install_requires=[
        'markdown',
    ],
    test_suite='nose.collector',
    tests_require=['nose', 'nose-cover3'],
)
