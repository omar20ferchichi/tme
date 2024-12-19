from setuptools import setup, find_packages

# Read the content of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tme",  # Replace with your package's name
    version="0.1.0",  # Initial release version
    author="Omar Ferchichi",  # Replace with your name
    author_email="ferchichiomar20@gmail.com",  # Replace with your email
    description="A short description of your project",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Required if using Markdown for README
    url="https://github.com/omar20ferchichi/tme",  # GitHub repo link
    packages=find_packages(),  # Automatically find all sub-packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Specify the license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version requirement
    license="MIT",  # Specify the license again
)
