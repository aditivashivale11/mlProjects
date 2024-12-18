from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def getRequirements(file_path: str)->List [str]:
    '''
    This funtion will return the list of requirements
    '''
    requirements =[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='mlprojects',
    version='0.0.1',
    author='Aditi',
    author_email='aditivashivale@gmail.com',
    packages=find_packages(),
    install_requires = getRequirements('requirements.txt')
)