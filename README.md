# cli_to_do_list_application
This Python program is a basic command-line To-Do List Application. The general idea is to provide users with a simple, text-based interface to manage their tasks.
The program uses a global list named tasks to store all the to-do items.

1. Core Functionality

Persistence: The load() function reads tasks from a file named tasks when the program starts, and the dump() function writes the current tasks back to the file when the user quits, ensuring tasks are saved between sessions.

2. Task Management

"add_task()" allows users to input new tasks and append them to the list.

"delete_task()" removes a task based on its index (number) in the list, including error handling for invalid input.

"mark_done()" appends the string [DONE] to a task to mark it as completed.

"view_task()" displays all current tasks with their index numbers.

3. User Interface

The "menu()" function displays the main options (Add, Delete, Mark Done, View, Quit) and handles user input validation, driving the application's flow within the "main()" function's loop.

This structure creates a functional, albeit simple, tool for managing a personal to-do list right from the command line.
