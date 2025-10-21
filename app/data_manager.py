import json
def load_json(file='task.json'):
    try:
        with open(file) as f:
            return [json.loads(line) for line in f]
    except FileNotFoundError:
        return None
def save_json(data, file='task.json'):
    with open(file, 'a') as f:
        for entry in data:
            f.write(json.dumps(entry) + "\n")
    