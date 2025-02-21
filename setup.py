# coding: utf-8
from os import path
import json
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(path.join(here, "requirements.txt"), encoding="utf-8") as f:
    install_requires = f.read().strip().split("\n")

# 从文件中读取JSON数据
with open("./czsc/publish.config.json", "r", encoding="utf-8") as file:
    public_config_data = json.load(file)

setup(
    name="czsc",
    version=public_config_data["version"],
    author=public_config_data["author"],
    author_email=public_config_data["email"],
    keywords=["缠论", "技术分析", "A股", "期货", "缠中说禅", "量化", "QUANT", "程序化交易"],
    description="缠中说禅技术分析工具",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache Software License",
    url="https://github.com/waditu/czsc",
    packages=find_packages(include=["czsc", "czsc.*"]),
    include_package_data=True,
    install_requires=install_requires,
    package_data={"": ["utils/china_calendar.feather", "utils/minutes_split.feather"]},
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    entry_points={
        "console_scripts": [
            "czsc = czsc.cmd:czsc",
        ],
    },
)
