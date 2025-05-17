import json
import os

TASK_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        return json.load(f)
    
# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2)