
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="OptimizationTestFunctions", 
    version="1.0.0",
    author="Demetry Pascal",
    author_email="qtckpuhdsa@gmail.com",
    maintainer = ['Demetry Pascal'],
    description="PyPI package containing collection of optimization test functions and some useful methods for working with them",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PasaOpasen/OptimizationTestFunctions",
    keywords=['optimization', 'evolutionary algorithms', 'fast', 'easy', 'evolution', 'generator', 'test', 'test-functions', '3D', 'functions'],
    packages = setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]#,
    #install_requires=['numpy']
    
    )





