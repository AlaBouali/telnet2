import sys,setuptools,os
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="telnetlib2",
    version="1.1.0",
    author="AlaBouali",
    author_email="trap.leader.123@gmail.com",
    description="simple telnet module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlaBouali/telnetlib2",
    python_requires=">=2.7",
    install_requires=[],
    packages=["telnetlib2"],
    license="MIT License",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License ",
    ],
)
