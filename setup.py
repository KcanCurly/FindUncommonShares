from setuptools import setup, find_packages

setup(
    name="FindUncommonShares",
    version="1.0.0",
    author="KcanCurly",
    description="A Python tool to find uncommon SMB shares on a network for penetration testing purposes",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KcanCurly/FindUncommonShares",
    packages=find_packages('finduncommonshares'),
    install_requires=[
        "impacket>=0.9.22",
        "xlsxwriter",
        "sectools>=1.4.1",
        "pycryptodome"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "FindUncommonShares=finduncommonshares:main",  
        ],
    },
)