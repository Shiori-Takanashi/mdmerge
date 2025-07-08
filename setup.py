from setuptools import setup, find_packages

setup(
    name="mdmerge",
    version="0.1.0",
    description="Markdown merge utility",
    packages=find_packages(),
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "mdmerge=cli.cli_main:run",
        ],
    },
    python_requires=">=3.8",
)
