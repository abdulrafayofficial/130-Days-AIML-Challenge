from collections import Counter
from functools import wraps
import time
import json
import os

tasks = []
SAVE_FILE = "tasks.json"


# ---------- Context Manager ----------
class File_Save:
    """Context manager that opens a file for reading/writing tasks and always closes it."""
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc, tb):
        if self.file:
            self.file.close()
        print('The file is closed!')
        # return False -> agar koi exception aaya to wo suppress nahi hoga
        return False


def save_tasks():
    with File_Save(SAVE_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)
    print('Tasks saved to file!')


def load_tasks():
    global tasks
    if os.path.exists(SAVE_FILE):
        with File_Save(SAVE_FILE, 'r') as f:
            content = f.read()
            tasks = json.loads(content) if content else []
    else:
        tasks = []


# ---------- Decorator ----------
def timer_dec(base_fn):
    @wraps(base_fn)
    def enhanced_fn(*args, **kwargs):
        start_time = time.time()
        result = base_fn(*args, **kwargs)

        # agar base_fn generator hai, to result ko yahin consume karke
        # asal kaam (yield wale) bhi timer ke andar measure ho jayega
        if hasattr(result, '__next__'):
            result = list(result)

        end_time = time.time()
        print(f"Task Time: {end_time - start_time:.6f} seconds")
        return result
    return enhanced_fn


# ---------- Core Functions ----------
@timer_dec
def addTask():
    task_to_add = input('Enter the Name of the task: ').lower()
    task_status = input('What is the status of the task: ')
    new_task = {"name": task_to_add, "status": task_status}
    tasks.append(new_task)
    print('Task Added!')
    save_tasks()


@timer_dec
def viewTask():
    if not tasks:
        yield 'No tasks yet!'
        return
    for index, task in enumerate(tasks, start=1):
        yield f"{index}. {task['name']} - {task['status']}"


@timer_dec
def completeTask():
    task_name = input('Enter task name to complete: ').lower()
    found = False
    for task in tasks:
        if task['name'] == task_name:
            task['status'] = 'Completed!'
            found = True
            break

    if found:
        print('Task marked as completed!')
        save_tasks()
    else:
        print('Task Not Found!')


@timer_dec
def deleteTask():
    del_task = input('Enter the name of the task you want to delete: ').lower()
    task_to_remove = None
    for task in tasks:
        if task['name'] == del_task:
            task_to_remove = task
            break

    if task_to_remove:
        tasks.remove(task_to_remove)
        print('Task Deleted!')
        save_tasks()
    else:
        print('Task not found!')


@timer_dec
def showStats():
    status_task = [task['status'] for task in tasks]
    print(Counter(status_task))


# ---------- Main Menu ----------
def main():
    load_tasks()

    while True:
        option = input('''
        Enter one of the following:
        1. Add Task
        2. View Tasks
        3. Complete Task
        4. Delete Task
        5. Show Stats
        6. Exit
        ''')

        if option == '1':
            print("Add Task selected")
            addTask()
        elif option == '2':
            print("View Tasks selected")
            for line in viewTask():
                print(line)
        elif option == '3':
            print("Complete Task selected")
            completeTask()
        elif option == '4':
            print("Delete Task selected")
            deleteTask()
        elif option == '5':
            print("Show Stats selected")
            showStats()
        elif option == '6':
            print("Exiting...")
            break
        else:
            print("Invalid option, try again")


if __name__ == '__main__':
    main()