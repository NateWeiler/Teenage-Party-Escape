import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="teenage"
    version="0.0.1",
    author=""Nathan Weiler,
    author_email="nateweiler84@gmail.com",
    url="https://github.com/NateWeiler/Teenage_Party_Escape",
    description="A teenagers escape from his home to go to a party",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
