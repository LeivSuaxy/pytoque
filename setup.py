from setuptools import setup, find_packages

setup(
    name="pytoque",
    version="0.2.0",
    packages=find_packages(),
    install_requires=[
        "certifi==2024.8.30",
        "charset-normalizer==3.4.0",
        "idna==3.10",
        "requests==2.32.3",
        "urllib3==2.2.3",
        "beautifulsoup4==4.13.3",
        "setuptools==75.6.0",
        "soupsieve==2.6",
        "typing_extensions==4.12.2",
    ],
    author="jleivsuaxy",
    author_email="jleivsuaxy@gmail.com",
    description="A package that facilitates requests and has some tools for the El-Toque API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LeivSuaxy/pytoque",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
