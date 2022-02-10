import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lifesimpack-AviationSFO",
    version="0.1-beta",
    author="Steven Weinstein",
    author_email="private",
    description="A life \'simulation\' package created as a joke.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AviationSFO/lifesimpack",
    project_urls={
        "Bug Tracker": "https://github.com/AviationSFO/lifesimpack/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GPL-3.0 License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)