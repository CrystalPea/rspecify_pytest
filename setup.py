from setuptools import setup

setup(
    name='pytest-easyread',
    description='pytest plugin that makes terminal printouts of the reports easier to read',
    long_description=open("README.md").read(),
    version='0.1.1',
    url='https://github.com/CrystalPea/pytest-easyread',
    download_url='https://github.com/CrystalPea/pytest-easyread/archive/0.1.tar.gz',
    license='BSD',
    author='Pea Tyczynska',
    author_email='m.a.tyczynska@gmail.com',
    py_modules=['pytest_easyread'],
    entry_points={'pytest11': ['easyread = pytest_easyread']},
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['pytest>=3.0.4'],
    keywords=['testing', 'readability', 'terminal'],
    classifiers=[
        "Framework :: Pytest",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Development Status :: 7 - Inactive",
    ]
)
