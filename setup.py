from setuptools import setup, find_packages

# Package metadata
NAME = "ArchaeTron"
VERSION = "0.1.0"
DESCRIPTION = "Your package description"
AUTHOR = "Dylan G Foley"
EMAIL = "thewookie@protonmail.com"
URL = "https://github.com/kodai_bot/ArchaeTron"

# Dependencies
REQUIRES = [
    # List your dependencies here, e.g.,
    # "numpy>=1.0",
]

# Extra dependencies (for optional features)
EXTRAS_REQUIRE = {
    # Define extra dependencies if needed, e.g.,
    # "dev": ["pytest"],
}

# Packages to include
PACKAGES = find_packages()

# Entry points (if your package includes any command-line scripts)
ENTRY_POINTS = {
    # Example:
    # 'console_scripts': [
    #     'your_script_name = your_package_name.module:main_function',
    # ],
}

# Long description (usually loaded from a README file)
with open("README.md", "r", encoding="utf-8") as readme_file:
    LONG_DESCRIPTION = readme_file.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=PACKAGES,
    install_requires=REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    entry_points=ENTRY_POINTS,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    classifiers=[
        # Add classifiers that describe your package (e.g., for PyPI)
    ],
)
