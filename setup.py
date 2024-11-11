from setuptools import setup, find_packages

setup(
    name="FindUncommonShares",
    version="1.0.0",
    author="p0dalirius",
    description="A tool to find uncommon SMB shares on a network for penetration testing",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/p0dalirius/FindUncommonShares",
    packages=find_packages(),
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
        "Intended Audience :: Science/Research",
        "Intended Audience :: System Administrators",
        "Topic :: Security",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "finduncommonshares=finduncommonshares:main",
        ],
    },
)
