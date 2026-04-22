from setuptools import setup, find_packages

HYPEN_DOT= "-e ."

def requirements(file_path:str):
    requirements=[]
    with open(file_path , 'r') as file:
        for line in file:
            req = line.strip()
          
            if req.startswith("-e"):
                continue
            requirements.append(req)
    return requirements


setup(
    name="ml_project",
    version="0.0.1",
    author="noor fatima",
    author_email="noorfatima0161@gmail.com",
    packages=find_packages(),
    install_requires=requirements("requirements.txt")
)