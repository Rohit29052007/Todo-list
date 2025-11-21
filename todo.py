
tasks=[]

def view_tasks():
    if not tasks:
        print("No tasks Yet/n")
        return 
    print("Your Tasks:")
    for i,t in enumerate(tasks,1):
        print(f"{i},{t}")
    print()

def add_tasks():
    task=input("Enter Your Task:")
    if task:
        tasks.append(task)
        print("Task Added")
    else:
        print("Empty task not Allowed")

def remove_tasks():
    view_tasks()
    if not tasks:
        return 
    try:
        num=int(input("Enter task number to remove:"))
        tasks.pop(num-1)
        print("Task Removed")
    except:
        print("Invalid Option")

def main():
    print("*****-------TO DO LIST-------*******")
    while True:    
        print("Actions: Add | View | Remove | Exit")
        cmd=input("Enter command:").lower()

        if cmd=="add":
            add_tasks()
        elif cmd=="view":
            view_tasks()
        elif cmd=="remove":
            remove_tasks()
        elif cmd=="exit":
            break
        else:
            print("Invalid Choice of Command!")

main()

