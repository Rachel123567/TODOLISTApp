import os

tasks = []

def load_tasks():
    """Loads tasks from a file, if available"""
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())

def save_tasks():
    """Saves tasks to a file"""
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(task):
    """Adds a new task to the list"""
    tasks.append(task)
    save_tasks()
    print(f"Task '{task}' added.")

def view_tasks():
    """Displays all tasks in the list"""
    if tasks:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No tasks found.")

def delete_task(task_number):
    """Deletes a task by its number in the list"""
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks()
        print(f"Task '{removed_task}' deleted.")
    else:
        print("Invalid task number.")

def show_menu():
    """Shows the menu of options"""
    print("\nTo-Do List App")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

def run():
    """Runs the main loop of the To-Do list app"""
    load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            try:
                task_number = int(input("Enter the task number to delete: "))
                delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting the To-Do list app.")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")

# Run the app
run()
