import subprocess
import sys
from setuptools import setup, find_packages
from setuptools.command.install import install


class InstallLocalPackage(install):
    def run(self):
        install.run(self)
        print("Running ops compilation...")
        subprocess.run(
            [
                'python',
                'deformable_detr/models/ops/compile/setup.py',
                'install'
            ],
            stdout=sys.stdout, stderr=sys.stderr, check=True,
        )


setup(
    name='deformable-detr',
    version='0.0.0',
    author="fundamentalvision",
    packages=find_packages(),
    cmdclass={'install': InstallLocalPackage},
)
