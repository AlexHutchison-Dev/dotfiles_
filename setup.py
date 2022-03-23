from setuptools import setup

setup(
    name="dotfiles",
    version="0.1.0",
    py_modules=["dotfiles"],
    install_requires=[
        "Click",
    ],
    entry_points={
        "console_scripts": [
            "dotfiles = dotfiles:cli",
        ],
    },
)
