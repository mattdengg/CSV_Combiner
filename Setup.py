from setuptools import setup, find_packages

setup(
    name='csv_combiner',
    version='1.0',
    description='Combined CSV files',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
    ],
    extras_require={
        'test': ['tk']
    }
)
