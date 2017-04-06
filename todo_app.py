import sys

#print(sys.argv)

def print_todos():
    todo_file = open("todo_data.txt")
    todos = todo_file.readlines()
    todo_file.close()
    if len(todos) == 0:
        print("no todos for today")
    else:
        for todo in range(1, len(todos) + 1):
            print(str(todo) + " - " + todos[todo - 1].rstrip())#leszedi a white spacet a txt file sorai vegerol


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

def add_todo():
    todo_file = open("todo_data.txt", "a")
    cont = "buy candy"
    todos = todo_file.writelines(cont)
    todo_file.close()

add_todo()

def controller(arg):
    if len(sys.argv) == 2:
        if sys.argv[1] == "-l":
            print_todos()
    else:
        print_help()

controller(sys.argv)
