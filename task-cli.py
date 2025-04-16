import os
import json
import sys
from datetime import datetime

file_path = "task_storage.json"

def load_tasks():
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump([], f)
        return []
    
    with open(file_path, "r") as f:
        try:
            return json.load(f)
        except:
            return []
        
def write_tasks(tasks):
    with open(file_path, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(description):
    tasks = load_tasks()
    id = new_id(tasks)
    new_task = {
        'id': id,
        'description': description,
        'status': "in-progress",
        'createdAt': datetime.now().isoformat(timespec='seconds'),
        'updatedAt': datetime.now().isoformat(timespec='seconds')
    }

    tasks.append(new_task)
    write_tasks(tasks)
    print(f"Task {description} created with id {id}.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Empty tasks list.")
    else:
        for task in tasks:
            print(f"Task Id: {task['id']}\n"
                  f"Description: {task['description']}\n"
                  f"Status: {task['status']}\n"
                  f"Created At: {datetime.fromisoformat(task['createdAt'])}\n"
                  f"Updated At: {datetime.fromisoformat(task['updatedAt'])}.\n")

def update_tasks(id, status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == int(id):
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat(timespec='seconds')
            print(f"Task {id} status updated as {status}")

    write_tasks(tasks)

def delete_tasks(id):
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        if task['id'] == int(id):
            tasks.pop(i)
            print(f"Task {id} has been deleted")
            break
            
    write_tasks(tasks)

def new_id(tasks):
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

def main():
    user_command = sys.argv[1]
    
    if user_command == "add":
        add_task(sys.argv[2]) # second argument is task description
    if user_command == "list":
        list_tasks()
    if user_command == "update":
        update_tasks(sys.argv[2], sys.argv[3]) #2nd arg is task id, 3rd arg is task status
    if user_command == "delete":
        delete_tasks(sys.argv[2]) #2nd arg is task id

if __name__ == "__main__":
    main()

    
        