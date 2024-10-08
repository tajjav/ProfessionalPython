def add_task(task):
    with open('tasks.txt', 'a') as file:
        file.write(task + "\n")
    print("Task added.")


def list_task():
    print("Tasks: ")
    with open('tasks.txt', 'r') as file:
        for number, task in enumerate(file, start=

        1):
            print(f"{number}. {task.strip()}")



def complete_task(task_number):
    tasks = []
    with open('tasks.txt', 'r') as file:
        tasks = file.readlines()
    try:
        completed_task = tasks.pop(task_number - 1)
        with open('completed.txt', 'a') as file:
            file.write(completed_task)
    except IndexError:
        print("Invalid task number.")
        return
    with open('tasks.txt', 'w') as file:
        file.writelines(tasks)
    print("Task completed.")


def delete_task(task_number):
    tasks = []
    with open('tasks.txt', 'r') as file:
        tasks = file.readlines()
    try:
        tasks.pop(task_number - 1)
    except IndexError:
        print("Invalid task number.")
        return
    with open('tasks.txt', 'w') as file:
        file.writelines(tasks)
    print("Task deleted.")


def main():
    while True:
        print("\nPyTasker - Simple Task Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            task = input("Enter task description: ")
            add_task(task)
        elif choice == '2':
            list_task()
        elif choice == '3':
            task_number = int(input("Enter task number to complete: "))
            complete_task(task_number)
        elif choice == '4':
            task_number = int(input("Enter task number to delete: "))
            delete_task(task_number)
        elif choice == '5':
            print("Exiting PyTasker.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()

