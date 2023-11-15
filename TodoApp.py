import datetime

tasks = []

def add_task():
    task_title = input("Enter task title: ")
    task_description = input("Enter task description: ")
    tasks.append({"title": task_title, "description": task_description, "created": datetime.datetime.now(), "completed": False})
    print("Task added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks to display.")
        return
    print("\n==== My Task ====")
    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Incomplete"
        print(f"{index}. {task['title']} - {task['description']} - {task['created']} - {status}")


def mark_task_complete():
    view_tasks()
    if not tasks:
        return
    task_number = int(input("Enter task number to mark as completed: "))
    if 0 < task_number <= len(tasks):
        tasks[task_number-1]["completed"]= True
    
    print("Task Updated successfully.")


def delete_task():
    view_tasks()
    if not tasks:
       return
    task_number = int(input("Enter task number to delete: "))
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number - 1)
    print("Task deleted successfully.")


def update_task():
    view_tasks()
    if not tasks:
        return
    task_number = int(input("Enter task number to update: "))
    if 0 < task_number <= len(tasks):
         task_title = input("Enter task title (Press Enter to skip): ")
         task_description = input("Enter task description (Press Enter to skip): ")
         print(task_title, task_description)
        
         if(len(task_title) > 0):
             tasks[task_number -1]["title"] = task_title
         if (len(task_description) > 0):
             tasks[task_number -1]["description"] = task_description
        
         print("Task updated successfully.")
             

while True:
    print("\n ===== Please choose an option =======")
    print("\nOption 1: Add Task \n Option 2: View All Task \n Option 3: Mark Complete \n Option 4: Update Task \nOption 5: Delete Task \n Option 6: Quit\n")
    option = int(input("Choose an option: "))
    if option == 1:
        add_task()
    elif option == 2:
        view_tasks()
    elif option == 3:
        mark_task_complete()
    elif option == 4:
        update_task()
    elif option == 5: 
        delete_task()
    elif option == 6:
        break
    else:
        print("Please choose an option")
     
