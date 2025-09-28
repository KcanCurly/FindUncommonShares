from setuptools import setup, find_packages

def read_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()

setup(
    name="FindUncommonShares",
    version="1.0.0",
    author="KcanCurly",
    description="A Python tool to find uncommon SMB shares on a network for penetration testing purposes",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KcanCurly/FindUncommonShares",
    packages=find_packages(),
    install_requires=read_requirements(),
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "FindUncommonShares=src.finduncommonshares:main",  
        ],
    },
)