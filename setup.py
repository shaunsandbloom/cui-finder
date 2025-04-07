from setuptools import setup, find_packages

setup(
    author = "Shaun Sandbloom",
    description = "A package for detecting Controlled Unclassified Information and Personally Identifiable Infromation in text",
    name = "cui_finder",
    packages = find_packages(include = ['cui_finder', 'cui_finder.*']),
    include_package_data = True,
    package_data = {'': ['*.json']},
    version = "0.1.0"
)
