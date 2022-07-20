import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="blackbear",
    version="0.0.1",
    author="Calvin DeBoer",
    author_email="cgdeboer@gmail.com",
    description=("TDB"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cgdeboer/blackbear",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
