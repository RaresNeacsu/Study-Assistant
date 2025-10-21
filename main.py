import sys
import json
from app.data_manager import load_json, save_json
from app.time_utilities import zile_deadline

cmd=input("Command(add, delete, list): ")

if(cmd=="add"):
    title=input("Title: ")
    deadline=input("Deadline(YYYY-MM-DD): ")
    save_json([{"Title":title, "Deadline":deadline}])

if(cmd=="delete"):
    title=input("Title to delete: ")
    tasks=load_json()
    for task in tasks:
        if task["Title"]==title:
            tasks.remove(task)
        with open(tasks, 'w') as f:
            for entry in tasks:
                f.write(json.dumps(entry) + "\n")

if(cmd=="list"):
    tasks=load_json()
    for task in tasks:
        zile_ramase = zile_deadline(task["Deadline"])
        print({task["Title"]}, "-", zile_deadline(task["Deadline"]),"zile ramase")