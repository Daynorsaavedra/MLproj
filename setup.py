from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='mlproject', # name of the project you can change
version='0.0.1', # version that needs to be aupdate it as you work 
author='daynor',
author_email='daynor@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)

## with this code you will get the installation of 
## all the packages need it for the project
## this code will read the requirements file and 
## will install all the packages listed there
## and will create the file mlproject.egg-info  