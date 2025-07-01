import datetime

todo_list = []

def show_menu():
    print("\n📋 TO-DO LIST MENU")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. Exit")

def view_tasks():
    if not todo_list:
        print("No tasks yet.")
        return
    for idx, task in enumerate(todo_list, 1):
        status = "✅" if task['completed'] else "❌"
        print(f"\nTask {idx}: {task['title']} [{status}]")
        print(f"  Description: {task['description']}")
        print(f"  Due Date: {task['due_date']}")
        print(f"  Priority: {task['priority']}")

def add_task():
    title = input("Enter task title: ")
    description = input("Enter description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (High/Medium/Low): ").capitalize()

    # Validate date
    try:
        datetime.datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "completed": False
    }
    todo_list.append(task)
    print("Task added.")

def update_task():
    view_tasks()
    task_num = int(input("\nEnter task number to update: ")) - 1
    if 0 <= task_num < len(todo_list):
        task = todo_list[task_num]
        task['title'] = input(f"New title ({task['title']}): ") or task['title']
        task['description'] = input(f"New description ({task['description']}): ") or task['description']
        task['due_date'] = input(f"New due date ({task['due_date']}): ") or task['due_date']
        task['priority'] = input(f"New priority ({task['priority']}): ") or task['priority']
        print("Task updated.")
    else:
        print("Invalid task number.")

def mark_completed():
    view_tasks()
    task_num = int(input("\nEnter task number to mark as completed: ")) - 1
    if 0 <= task_num < len(todo_list):
        todo_list[task_num]['completed'] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    task_num = int(input("\nEnter task number to delete: ")) - 1
    if 0 <= task_num < len(todo_list):
        deleted = todo_list.pop(task_num)
        print(f"Deleted task: {deleted['title']}")
    else:
        print("Invalid task number.")

# Main Loop
while True:
    show_menu()
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        mark_completed()
    elif choice == "5":
        delete_task()
    elif choice == "6":
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
