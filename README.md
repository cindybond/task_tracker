# Task Tracker CLI App

A simple Command Line Interface (CLI) project to track and manage tasks. [Project Link] (https://roadmap.sh/projects/task-tracker)

## Features
- Add a new task
- List all tasks
- List tasks based on their status
- Update task's status
- Delete task

## Installation
Since this is written in Python, make sure it is installed in your system. 
task-cli is installed via pip. Here are the steps:
1. Clone the repository
```
git clone https://github.com/cindybond/task_tracker.git
cd task_tracker
```
2. Install the project 
```
pip install -e .
```

## Usage
### Add a new task 
```
# Command to add a new task 
task-cli add "Task description"

# Example use
task-cli add "Wash dishes" 
```

### List Task
```
# Command to list tasks
task-cli list <status>

# Example to list all tasks
task-cli list

# Example to list in-progress tasks
task-cli list in-progress
```

### Update Task
```
# Command to update tasks
task-cli update <id> <status>

# Example to update task
task-cli update 1 done
```

### Delete Task
```
# Command to delete tasks
task-cli delete <id>

# Example to delete task
task-cli delete 1
```

## License 
This project is licensed under the MIT License - see the [LICENSE](license) file for details.
