from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r") as f:
    long_description = f.read()

VERSION = '1.0.2'
DESCRIPTION = 'Pre-written Classes for pygame'
# Setting up
setup(
    name="indiedev",
    url = "https://github.com/NotSujal/Indie",
    version=VERSION,
    author="Sujal Choudhari (NotSujal)",
    author_email="<sjlchoudhari@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description = long_description,
    packages=find_packages(),
    install_requires=['pygame'],
    keywords=['python', 'pygame', 'engine', 'pre-written code'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
