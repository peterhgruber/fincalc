from setuptools import setup, find_packages

setup(
    name="fincalc",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        # Add your package dependencies here
        "numpy",
        "scipy",
        "pandas"
    ],
    # Additional metadata about your package
    author="Peter Gruber, Mattia Biancaterra",
    author_email="peter.gruber@usi.ch",
    description="A simple example for a Python package in Finance",
    keywords="interest, finance, present value",
    url="https://github.com/peterhgruber/fincalc",  # Project home page
)
