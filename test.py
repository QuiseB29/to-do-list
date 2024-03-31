introduction = "Welcome to the To-Do List App!"
print(introduction)
tasks = []

def add_task(tasks, task):
    tasks.append({"task": task, "completed": False})
    print("Task added.")


def view_tasks(tasks):
    if tasks:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            status = " (Completed)" if task["completed"] else ""
            print(f"{index}. {task['task']}{status}")
    else:
        print("To-Do List is empty.")


def delete_task(tasks):
    try:
        if tasks:
            view_tasks(tasks)
            task_index = int(input("Enter the number of the task to delete: ")) - 1
            if 0 <= task_index < len(tasks):
                removed_task = tasks.pop(task_index)
                print(f"Task '{removed_task['task']}' removed.")
    except ValueError:
        print("invalid input enter number")


def mark_task(tasks):
    try:
        if tasks:
            view_tasks(tasks)
            task_index = int(input("Enter the number of the task to mark as completed: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["completed"] = True
                print("Task marked as completed.")
    except ValueError:
        print("Invalid character input number")


while True:
    print("\nPlease select one of the following options:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(tasks, task)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        mark_task(tasks)
    elif choice == "4":
        delete_task(tasks)
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
        
        
    ##In this project, you will apply your Python programming skills to create a functional To-Do List Application from scratch. 
# The objective of this project is to reinforce your understanding 
# of Python syntax, data types, control structures, functions, and error handling 
# while building a practical and interactive application.
