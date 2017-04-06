import sys

#print(sys.argv)

def print_todos():
    todo_file = open("todo_data.txt")
    todos = todo_file.readlines()
    todo_file.close()
    for todo in range(1, len(todos) + 1):
        print(str(todo) + " - " + todos[todo - 1].rstrip())

def print_help():
    help_content = ["Python Todo application",
                    "=======================",
                    "Command line arguments:",
                    " -l   Lists all the tasks",
                    " -a   Adds a new task",
                    " -r   Removes an task",
                    " -c   Completes an task"]

    for content in help_content:
        print(content)


if len(sys.argv) == 2:
    print_todos()
else:
    print_help()
