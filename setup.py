from setuptools import setup, find_packages

setup(
    name='tryexcept',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas'
    ],
    author='Davide Di Grande',
    author_email='davidedigrande.dev@gmail.com',
    description='See README',
    url='https://github.com/davidedigrande/exception_handler_decorator',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
