import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

dev_requirements = [
    "geoip2",  # for testing GeoIP2
    "pytest",
    "pytest-cov",
    "pytest-django",
]

setup(
    name="django-qsessions",
    version="1.0.1",
    description="Extended session backends for Django",
    long_description=README,
    author="Mohammad Javad Naderi",
    url="https://github.com/QueraTeam/django-qsessions",
    download_url="https://pypi.python.org/pypi/django-qsessions",
    license="MIT",
    packages=find_packages(".", include=("qsessions", "qsessions.*")),
    include_package_data=True,
    install_requires=["Django>=1.11", "user-agents>=1.1.0", "django-ipware>=2.0.0"],
    extras_require={"dev": dev_requirements},
    tests_require=dev_requirements,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP :: Session",
        "Topic :: Security",
    ],
)
