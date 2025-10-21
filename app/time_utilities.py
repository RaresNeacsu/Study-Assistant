from datetime import datetime

def zile_deadline(deadline_str):
    deadline = datetime.strptime(deadline_str, "%Y-%m-%d")
    today = datetime.now()
    delta = (deadline - today).days
    return delta