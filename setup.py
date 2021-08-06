from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_desc = fh.read()


setup(
    name='colouringIDLE',
    version='0.1',
    description="Using Coloured Text in IDLE",
    long_description=long_desc,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        ],
    keywords='',
    author='Aiyush Gupta',
    author_email='ooshimus@gmail.com',
    url='ooshimus.com',
    license='MIT',
    packages=setuptools.find_packages(),
    namespace_packages=[],
    include_package_data=False,
    zip_safe=False,
    install_requires=[],
    tests_require=[],
    entry_points={}
)
