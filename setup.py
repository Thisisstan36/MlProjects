from setuptools import find_packages, setup
from typing import List


HYPEHN_E= '-e.'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open('requirements.txt') as file:
        requirements=file.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if HYPEHN_E in requirements:
            requirements.remove(HYPEHN_E)

    return requirements

setup(
    name='MLProject',
    version='0.0.1',
    author='Jayesh',
    author_email ='jayeshnikam4@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)