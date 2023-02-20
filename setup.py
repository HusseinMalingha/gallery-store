from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    description="a micro bloging app",
    author="osep",
    author_email='husseinmalingha@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)