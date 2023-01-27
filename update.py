import os
import shutil
import json

# marks the latest directory with a flag 

def find_latest():
    """find the directory with the latest date"""
    dirnames = []
    for dirname in os.listdir('.'):
        if dirname[0:1].isdigit() and dirname[2] == '-':
            dirnames.append(dirname)
    latest = max(dirnames, key=os.path.getctime)
    
    return latest


def rename_dir():
    latest = find_latest()
    if not latest.endswith(' - 🚩 latest'):
        os.rename(latest, f'{latest} - 🚩 latest')
        print('Directory already exists')

        try:
            old_latest = json.load(open('update.json'))
        except json.decoder.JSONDecodeError:
            old_latest = ''
            print('No previous latest directory found')

        if os.path.exists(f'{old_latest} - 🚩 latest'):
            os.rename(f'{old_latest} - 🚩 latest', old_latest)
        
        with open ('update.json', 'w') as f:
            json.dump(latest, f)
        print(f'Renamed directory to {latest} - 🚩 latest')
    
    else:
        print('Directory already exists')

rename_dir()

