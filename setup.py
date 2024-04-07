from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "Truly random generated numbers, char, string..."
LONG_DESCRIPTION = "Generate truly random numbers, char, string..."

# Setting up
setup(
    name="brandom",
    version=VERSION,
    author="Leonardix007 (Leonardo Ricci)",
    author_email="<leonardoricci775@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'random', 'real random', 'true random'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
