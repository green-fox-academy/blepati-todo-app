import sys

#print(sys.argv)

def print_help():
    help_content = ["Python Todo application",
                    "=======================",
                    "Command line arguments:",
                    " -l   Lists all the tasks",
                    " -a   Adds a new task, note: your task need to be inside double quotemarks",
                    " -r   Removes an task",
                    " -c   Completes an task"]

    for content in help_content:
        print(content)

#def read_todos():
    #todo_file = open("todo_data.txt", "r")
    #todos = todo_file.readlines()
    #todo_file.close()

def print_todos():
    todo_file = open("todo_data.txt", "r")
    todos = todo_file.readlines()
    todo_file.close()
    if len(todos) == 0:
        print("no todos for today")
    else:
        for todo in range(1, len(todos) + 1):
            print(str(todo) + " - " + todos[todo - 1].rstrip())#leszedi a white spacet a txt file sorai vegerol

def add_todo():
    todo_file = open("todo_data.txt", "a")
    if len(sys.argv) > 2:
        cont = str(sys.argv[2]) + "\n"
        todos = todo_file.writelines(cont)
        todo_file.close()
        print("new task added")
    else:
        print("you did not add task yet")

def delete_todo():
    todo_file = open("todo_data.txt", "r")
    todos = todo_file.readlines()
    todo_file.close()
    remove_todos = open("todo_data.txt", "w")
    remove_todo_num = int(sys.argv[2])
    for todo in range(len(todos)):
        if todo == remove_todo_num - 1:
            pass
        else:
            remove_todos.write(todos[todo])

def controller(arg):
    if len(sys.argv) >= 2:
        if sys.argv[1] == "-l":
            print_todos()
        elif sys.argv[1] == "-a":
            add_todo()
        elif sys.argv[1] == "-r":
            delete_todo()
    else:
        print_help()

controller(sys.argv)
