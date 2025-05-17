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

# Display task list
def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for i, task in enumerate(tasks):
        status = "✔️" if task["done"] else "❌"
        print(f"{i + 1}. [{status}] {task['title']}")

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added.")