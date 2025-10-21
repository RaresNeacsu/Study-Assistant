import json
import os

BASEDIR = os.path.dirname(os.path.dirname(__file__))
BASETASKFILE = os.path.join(BASEDIR,".gitignore", 'task.json')

def load_json(file=BASETASKFILE):
    try:
        with open(file) as f:
            return [json.loads(line) for line in f]
    except FileNotFoundError:
        return None
def save_json(data, file=BASETASKFILE):
    with open(file, 'a') as f:
        for entry in data:
            f.write(json.dumps(entry) + "\n")
    