from setuptools import setup, find_packages

setup(
    name="pytoque",  # Nombre del paquete
    version="0.1.1",  # Versión inicial
    packages=find_packages(),  # Encuentra todos los subpaquetes automáticamente
    install_requires=[
        "certifi==2024.8.30",
        "charset-normalizer==3.4.0",
        "idna==3.10",
        "requests==2.32.3",
        "urllib3==2.2.3",
    ],  # Dependencias externas (si tienes alguna)
    author="jleivsuaxy",
    author_email="jleivsuaxy@gmail.com",
    description="A package that facilitates requests and has some tools for the El-Toque API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LeivSuaxy/pytoque",  # (Opcional) Repositorio del proyecto
    classifiers=[  # (Opcional) Información adicional
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",  # Versión mínima de Python
)
