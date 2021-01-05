import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plato",
    version="0.0.1",
    author="2B3E",
    author_email="sungjin@mail.hongik.ac.kr",
    description="Dialogue engine for language education",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/2B3E/plato",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

