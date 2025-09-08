from setuptools import find_packages, setup

setup(
    name="dify_plugin",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "dify_plugin",
    ],
    extras_require={
        "dev": [
            "black",
            "flake8",
            "pytest",
            "pre-commit",
        ],
    },
)
