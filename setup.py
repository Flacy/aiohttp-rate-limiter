from setuptools import find_packages, setup


setup(
    name='aiohttp-rate-limiter',
    packages=['aiohttp_rate_limiter'],
    version='0.0.2',
    author='Flacy',
    author_email='me@flacy.me',
    description='A library for control and limiting requests with aiohttp framework',
    url='https://github.com/Flacy/aiohttp-rate-limiter',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        'Development Status :: 3 - Alpha'
    ],
    python_requires='>=3.7'
)
