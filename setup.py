from pathlib import Path

from setuptools import find_packages, setup

setup(
    name="tryexcept-decorator",
    version="0.0.4",
    author="Davide Di Grande",
    author_email="davidedigrande.dev@gmail.com",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    project_urls={"Source": "https://github.com/davidedigrande/tryexcept-decorator"},
)
