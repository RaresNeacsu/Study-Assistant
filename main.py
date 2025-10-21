from app.data_manager import load_json, save_json
from app.time_utilities import zile_deadline

save_json([{"Title": "Examen Algebra", "Deadline": "2025-11-17"}])
for task in load_json():
    zile_ramase = zile_deadline(task["Deadline"])
    print({task["Title"]}, "-", zile_deadline(task["Deadline"]),"zile ramase")