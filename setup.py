from setuptools import setup,find_packages


def get_requires(file_path:str):
    requires=[]
    with open(file_path) as f:
        requires=f.readlines()
        requires=[require.replace('\n','') for require in requires]
        if '-e .' in requires:
            requires.remove('-e .')
    return requires

setup(
    
    name='Whatsapp Text Analyzer',
    version=1.0,
    author='Ayazulhaq Yousafzai',
    author_email='www.ayazkhan.com.21@gmail.com',
    description='End to End Whatsapp Text Analyzer',
    install_requires=get_requires('requirements.txt'),
    packages=find_packages()
    
)