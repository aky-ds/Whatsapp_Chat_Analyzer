import os
from pathlib import Path
list_of_files=[
    'Deployed_App.py',
    'setup.py',
    'Preprocessing.py',
    'stats.py',
    'requirements.txt',
    'Whatsapp_data/__init__.py',

]


for file in list_of_files:
    file_path=Path(file)
    file_dir,file_name=os.path.split(file_path)
    if file_dir !="":
        os.makedirs(file_dir,exist_ok=True)
    elif not os.path.exists(file_path):
        with open(file_path,'w') as x:
            pass
