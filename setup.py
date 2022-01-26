from setuptools import setup, find_packages
from setuptools.command.install import install

import subprocess

class InstallLocalPackage(install):
    def run(self):
        install.run(self)
        subprocess.call(
            "python models/ops/compile/setup.py install", shell=True
        )


setup(
    name='deformable-detr',
    version='0.0.0',
    author="fundamentalvision",
    packages=find_packages(),
    cmdclass={ 'install': InstallLocalPackage },
)
