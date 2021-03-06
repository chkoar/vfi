#! /usr/bin/env python
"""A template for scikit-learn compatible packages."""

import os

from setuptools import find_packages, setup

ver_file = os.path.join("vfi", "_version.py")
with open(ver_file) as f:
    exec(f.read())

DISTNAME = "vfi"
DESCRIPTION = "Classification by Voting Feature Intervals in Python"
with open("README.rst", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()
MAINTAINER = "Christos K. Aridas"
MAINTAINER_EMAIL = "ichkoar@gmail.com"
URL = "https://github.com/chkoar/vfi"
LICENSE = "MIT"
DOWNLOAD_URL = "https://github.com/chkoar/vfi"
VERSION = __version__
INSTALL_REQUIRES = ["numpy", "scipy", "scikit-learn"]
CLASSIFIERS = [
    "Intended Audience :: Science/Research",
    "Intended Audience :: Developers",
    "License :: OSI Approved",
    "Programming Language :: Python",
    "Topic :: Software Development",
    "Topic :: Scientific/Engineering",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX",
    "Operating System :: Unix",
    "Operating System :: MacOS",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
]
EXTRAS_REQUIRE = {
    "tests": ["black", "flake8", "invoke", "pytest", "pytest-cov"],
    "docs": [
        "invoke",
        "matplotlib",
        "numpydoc",
        "sphinx",
        "sphinx-gallery",
        "sphinx_rtd_theme",
    ],
}

setup(
    name=DISTNAME,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    url=URL,
    version=VERSION,
    download_url=DOWNLOAD_URL,
    long_description=LONG_DESCRIPTION,
    zip_safe=False,  # the package can run out of an .egg file
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
)
