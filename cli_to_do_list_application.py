import sys
tasks = []

def load():
    global tasks
    with open('tasks','r') as t:
        tasks = [task.rstrip() for task in t.readlines()]

def dump():
    global tasks
    with open('tasks','w') as t:
        for task in tasks: 
            t.write("{}\n".format(task))
    
def add_task():
    global tasks
    while True:
        task = input("Enter a task you want to add to your list, and <enter> if finished: ")
        if not task: break
        tasks.append(task)
        print("'{}' added to your list".format(task))
    print()

def delete_task():
    global tasks
    while True:
        try:
            index = input("Enter the index of the task you want to remove to your list, and <enter> if finished: ")
            if index == '': break
            index = int(index) - 1
            print("'{}' has been removed".format(tasks.pop(index)))
        except IndexError:
            print("Error: Invalid index")
        except ValueError:
            print("Error: Index is not an integer")
    print()

def mark_done():
    global tasks
    while True: 
        try:
            index = input("Enter the index of the task you want to mark as done on your list, and <enter> if finished: ")
            if index == '': break
            index = int(index) - 1
            if "[DONE]" in tasks[index]:
                print("Error: Task is already marked as done")
                continue
            tasks[index] += " [DONE]"
            print("'{}' has been marked as done".format(tasks[index]))
        except IndexError:
            print("Error: Invalid index")
        except ValueError:
            print("Error: Index is not an integer")
    print()

def view_task():
    if not tasks: print("No task to do")
    else:
        for n,task in enumerate(tasks,1): print("{}. {}".format(n,task))
    print()

def quit():
        dump()
        sys.exit()

def menu():
    print("-----Main Menu-----")
    print("1. Add a task")
    print("2. Delete a task")
    print("3. Mark done a task")
    print("4. View tasks")
    print("5. Quit")
    
    choice = input("\nEnter the index of the operation you want to do: ")
    try:
        if int(choice) not in range(1,6):
            print("Error: Invalid option")
        else:
            return choice
    except ValueError:
        print("Error: Invalid option")

def main():
    load()
    print("--------------------------------------------------")
    print("Welcome to the COMMAND-LINE TO-DO LIST APPLICATION")
    print("--------------------------------------------------")
    while True:
        match(menu()):
            case '1':
                add_task()
            case '2':
                delete_task()
            case '3':
                mark_done()
            case '4':
                view_task()
            case '5':
                quit()

if __name__ == "__main__":
    main()