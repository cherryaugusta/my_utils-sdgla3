from setuptools import setup, find_packages

# Setup configuration for packaging and distribution
setup(
    name="my_utils",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Reusable utility package for validation and formatting",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cherryaugusta/my_utils-sdgla3.git",
    packages=find_packages(),
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
)
