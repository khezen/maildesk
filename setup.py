import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="maildesk",
    version="0.1.1",
    author="Guillaume Simonneau",
    author_email="simonneaug@gmail.com",
    description="email python library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/khezen/maildesk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)