from setuptools import setup, find_packages

setup(
    name='intercode',
    version='0.1',
    packages=find_packages(),
    package_dir={'': '.'},
    install_requires=[
        # Add any dependencies required by your package here
    ],
    include_package_data=True,
)
