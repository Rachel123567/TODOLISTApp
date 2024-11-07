import pickle

tasks = []

def load_tasks():
    """Loads tasks from a file if it exists"""
    global tasks
    try:
        with open("tasks.pkl", "rb") as f:
            tasks = pickle.load(f)
    except FileNotFoundError:
        tasks = []

def save_tasks():
    """Saves tasks to a file"""
    with open("tasks.pkl", "wb") as f:
        pickle.dump(tasks, f)

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")
    save_tasks()

def delete_task(task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' deleted.")
        save_tasks()
    else:
        print("Invalid task number.")

# Load tasks when the
