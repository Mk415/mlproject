from setuptools import find_packages, setup
from typing import List
hyphen="-e ."
def get_req(file_path:str)->List[str]:
    """
    takes the file location
    we open it and iterate over it and
    then pass it as a list to the install_requires object"""
    req=[]
    with open(file_path) as file_obj:
        req=file_obj.readlines()
        req=[i.replace("\n","") for i in req]
        if hyphen in req:
            req.remove(hyphen)
        return req
setup(
    name="MLproject",
    version="0.0.1",
    author="Khundmeer",
    author_email="mkjunaidd@gmail.com",
    packages=find_packages(), # finds where the packages needs to be installed
    install_requires=get_req("requirements.txt") #takes requirements.txt as the parameter

)