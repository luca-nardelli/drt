import os

from setuptools import setup, find_packages
from setuptools.command.install import install
import shutil

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        for obj in ['build', 'dist', 'drt.egg-info']:
            if os.path.exists(obj):
                shutil.rmtree(obj)
            print("Removed {}".format(obj))


setup(
    name="drt",
    version="0.1",
    packages=find_packages(),
    scripts=['drt'],

    author='Luca Nardelli',
    author_email='luca.nardelli@protonmail.com',
    description="Docker Repository management Tool",

    cmdclass={
        'install': PostInstallCommand
    }
)
