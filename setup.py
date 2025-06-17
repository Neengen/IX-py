from setuptools import setup, find_packages

setup(
    name="ix-py",
    version="0.1.0",
    description="Zero-dependency Python environment and dependency manager",
    author="Bryce Wooster",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "ix=ix_py.__main__:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Topic :: Software Development :: Build Tools"
    ],
    python_requires=">=3.8",
)
