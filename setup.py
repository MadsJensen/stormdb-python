import os
from setuptools import setup, Command


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# get the version (don't import mne here, so dependencies are not needed)
version = None
with open(os.path.join('stormdb', '__init__.py'), 'r') as fid:
    for line in (line.strip() for line in fid):
        if line.startswith('__version__'):
            version = line.split('=')[1].strip().strip('\'')
            break
if version is None:
    raise RuntimeError('Could not determine version')


class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')

setup(
    name="stormdb",
    version=version,
    author="Christopher Bailey",
    author_email="cjb@cfin.au.dk",
    description=("Tools for accessing StormDb @ CFIN"),
    license="MIT",
    keywords="code",
    url="https://github.com/meeg-cfin/stormdb-python.git",
    packages=['stormdb', 'stormdb.process'],
    scripts=['bin/submit_to_cluster',
             'bin/cfin_flash_bem',
             'bin/cfin_watershed_bem',
             'bin/cfin_organize_dicom'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    cmdclass={
        'clean': CleanCommand,
    }

)
