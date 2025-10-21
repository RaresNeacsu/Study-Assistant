from datetime import datetime
deadline=datetime.strptime("2025-12-01", "%Y-%m-%d")
today=datetime.now()
delta=(deadline-today).days
print(f"Days until deadline: {delta}")