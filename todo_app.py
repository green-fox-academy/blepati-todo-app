import sys

#print(sys.argv)

if len(sys.argv) == 2:
    todo_file = open("todo_data.txt")
    todos = todo_file.readlines()
    for todo in range(1, len(todos) + 1):
        print(str(todo) + " - " + todos[todo - 1].rstrip())
else:
    print("Python Todo application")
    print("=======================")
    print("Command line arguments:")
    print(" -l   Lists all the tasks")
    print(" -a   Adds a new task")
    print(" -r   Removes an task")
    print(" -c   Completes an task")
