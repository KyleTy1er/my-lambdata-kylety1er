# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="my-lambdata-kylety1er", # the name that you will install via pip
    version="6.0",
    author="Kyle Yates",
    author_email="kyates2861@gmail.com",
    description="First package upload",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/KyleTy1er/my-lambdata-kylety1er",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)