tasks = []

def view_tasks():
    if not tasks:
        print("No tasks yet.\n")
        return 
    print("Your Tasks:")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")
    print()

def add_tasks():
    task = input("Enter your task: ")
    if task:
        tasks.append(task)
        print("Task added.\n")
    else:
        print("Empty task is not allowed.\n")

def remove_tasks():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to remove: "))
        tasks.pop(num - 1)
        print("Task removed.\n")
    except:
        print("Invalid option.\n")

def main():
    print("*****------- TO-DO LIST -------*****")
    while True:
        print("Actions: Add | View | Remove | Exit")
        cmd = input("Enter command: ").lower()

        if cmd == "add":
            add_tasks()
        elif cmd == "view":
            view_tasks()
        elif cmd == "remove":
            remove_tasks()
        elif cmd == "exit":
            break
        else:
            print("Invalid choice!\n")
            continue

        # ✔ Ask if the user wants to continue
        ch = input("Do you want to continue? (Yes/no): ").lower()
        if ch not in ("yes", "y"):
            print("Thank you for using the To-Do List!")
            break

main()
