import json
def save_task(task):
    with open('task.json', 'w') as f:
        f.write(json.dumps(task)+ "\n")
save_task({"title":"Examen Mate", "deadline":"2025-12-01", "duration":120})
