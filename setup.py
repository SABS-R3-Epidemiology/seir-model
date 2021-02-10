#
# seirmo setuptools script
#
from setuptools import setup, find_packages


def get_version():
    """
    Get version number from the seirmo module.
    The easiest way would be to just ``import seirmo ``, but note that this may  # noqa
    fail if the dependencies have not been installed yet. Instead, we've put
    the version number in a simple version_info module, that we'll import here
    by temporarily adding the oxrse directory to the pythonpath using sys.path.
    """
    import os
    import sys

    sys.path.append(os.path.abspath('seirmo'))
    from version_info import VERSION as version
    sys.path.pop()

    return version


def get_readme():
    """
    Load README.md text for use as description.
    """
    with open('README.md') as f:
        return f.read()


setup(
    # Module name (lowercase)
    name='seirmo',

    # Version
    version=get_version(),

    description='This is a one-week project in which we are using SEIR model to model the outbreak of an infectious disease.',  # noqa

    long_description=get_readme(),

    license='BSD 3-Clause "New" or "Revised" License',

    # author='',

    # author_email='',

    maintainer='',

    maintainer_email='',

    url='https://github.com/SABS-R3-Epidemiology/seirmo.git',

    # Packages to include
    packages=find_packages(include=('seirmo', 'seirmo.*')),
    include_package_data=True,

    # List of dependencies
    install_requires=[
        # Dependencies go here!
        'dash==1.17.0',
        'dash-bootstrap-components==0.11.0',
        'dash-core-components==1.13.0',
        'dash-daq==0.5.0',
        'dash-html-components==1.1.1',
        'numpy>=1.8',
        'pandas',
        'plotly',
        'scipy',
    ],
    extras_require={
        'docs': [
            # Sphinx for doc generation. Version 1.7.3 has a bug:
            'sphinx>=1.5, !=1.7.3',
            # Nice theme for docs
            'sphinx_rtd_theme',
        ],
        'dev': [
            # Flake8 for code style checking
            'flake8>=3',
        ],
    },
)