import json
import os

TASK_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file)

def add_task(tasks, task):
    tasks.append({'task': task, 'completed': False})
    save_tasks(tasks)

def view_tasks(tasks):
    for idx, task in enumerate(tasks):
        status = 'Done' if task['completed'] else 'Pending'
        print(f"{idx + 1}. {task['task']} [{status}]")

def update_task(tasks, index, completed):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = completed
        save_tasks(tasks)

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            view_tasks(tasks)
            index = int(input("Enter task number to update: ")) - 1
            completed = input("Mark as completed? (y/n): ").lower() == 'y'
            update_task(tasks, index, completed)
        elif choice == '4':
            view_tasks(tasks)
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(tasks, index)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
