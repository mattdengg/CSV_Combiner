from setuptools import setup

setup(
    name='csv_combiner',
    version='1.0',
    description='Combined CSV files',
    packages=['CSV_Combiner'],
    install_requires=[
        'pandas',
        'numpy',
    ],
    extras_require={
        'test': ['tk']
    }
)