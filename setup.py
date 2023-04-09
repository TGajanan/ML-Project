from setuptools import find_packages,setup
from typing import List


hypen_e_dot='-e .' #this line for removeing ingoring the -e
def get_requirements(file_path:str)->List[str]:
    '''This function will return the all requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]  #for replacing the \
        
        if hypen_e_dot in requirements:    
            requirements.remove(hypen_e_dot) #To ignoring the -e
    return requirements


setup(
    name='MLProject',
    version='0.0.1',
    author='Gajanan',
    Author_email='gajanantodetti1998@gmail.com',
    packages=find_packages(), 
    install_requires=get_requirements('requirements.txt')  #to install libraries 
)