# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
#
# TASK: Console-Based To-Do List Application
#
# Build a simple to-do list program that runs entirely in the console and
# allows the user to manage their tasks interactively using a menu.
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Task
#      - Prompt the user to type a task description.
#      - Add it to the list and confirm it was added.
#
#   2. View All Tasks
#      - Display all tasks currently in the list, numbered from 1.
#      - If the list is empty, print a friendly message saying so.
#
#   3. Delete a Task
#      - Show the list of tasks with their numbers.
#      - Ask the user which task number they want to remove.
#      - Remove the task and confirm the deletion.
#      - If the task number is invalid, print an error message.
#
#   4. Quit
#      - End the program with a farewell message.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        TO-DO LIST MENU
#   ============================
#   1. Add task
#   2. View tasks
#   3. Delete task
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Enter task: Buy groceries
#   Task added: "Buy groceries"
#
#   Enter your choice (1-4): 1
#   Enter task: Study for exams
#   Task added: "Study for exams"
#
#   Enter your choice (1-4): 2
#   Your Tasks:
#   1. Buy groceries
#   2. Study for exams
#
#   Enter your choice (1-4): 3
#   Enter task number to delete: 1
#   Task "Buy groceries" has been removed.
#
#   Enter your choice (1-4): 4
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store tasks in a Python list.
# - Use a loop to keep the menu running until the user chooses to quit.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices gracefully (print an error, do not crash).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def add_task(tasks):
    task_description = input("Enter task: ").strip()

    if task_description == "":
        print("Error: Task description cannot be empty.")
    else:
        tasks.append(task_description)
        print('Task added: "' + task_description + '"')


def view_tasks(tasks):
    if len(tasks) == 0:
        print("Your to-do list is empty.")
    else:
        print("\nYour Tasks:")

        for task_number in range(len(tasks)):
            print(str(task_number + 1) + ".", tasks[task_number])


def delete_task(tasks):
    if len(tasks) == 0:
        print("There are no tasks to delete.")
        return

    view_tasks(tasks)

    try:
        task_number = int(input("Enter task number to delete: "))

        if task_number < 1 or task_number > len(tasks):
            print("Error: Invalid task number.")
        else:
            removed_task = tasks.pop(task_number - 1)
            print('Task "' + removed_task + '" has been removed.')

    except ValueError:
        print("Error: Please enter a valid task number.")


def display_menu():
    print("\n============================")
    print("     TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


def main():
    tasks = []

    while True:
        display_menu()
        menu_choice = input("Enter your choice (1-4): ")

        if menu_choice == "1":
            add_task(tasks)

        elif menu_choice == "2":
            view_tasks(tasks)

        elif menu_choice == "3":
            delete_task(tasks)

        elif menu_choice == "4":
            print("Goodbye!")
            break

        else:
            print("Error: Please enter a number from 1 to 4.")


main()