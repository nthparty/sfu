from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read().replace(".. include:: toc.rst\n\n", "")

# The lines below can be parsed by `docs/conf.py`.
name = "sfu"
version = "1.0.2"

setup(
    name=name,
    version=version,
    packages=[name,],
    install_requires=[],
    license="MIT",
    url="https://github.com/nthparty/sfu",
    author="Ben Getchell",
    author_email="bengetch@gmail.com",
    description="Snowflake URI utility library that supports extraction of Snowflake "
                "configuration data and method parameters from Snowflake resource URIs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    test_suite="nose.collector",
    tests_require=["pytest"],
)