import setuptools

with open("README.md", "r", encoding="utf-8") as fh:#
    long_description = fh.read()

__version__ = "0.0.1"

REPO_NAME = "rp_text_summarizer"
AUTHOR_USER_NAME = "Pangani"
SRC_REPO = "rp_text_summarizer"
AUTHOR_EMAIL = "roypangani@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="a python package for summarizing text using NLP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)