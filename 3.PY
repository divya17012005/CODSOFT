tasks = []

def add_task(task):
    tasks.append(task)
    print(f'Task "{task}" added.')

    def view_tasks():
        if not tasks:
            print("No tasks available.")
        else:
                print("\nYour To-Do List")
                for idx, task in enumerate(tasks, start=1):
                    print(f'{idx}. {task}')

def main():
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()