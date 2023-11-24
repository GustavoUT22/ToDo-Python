# pylint: disable=missing-function-docstring
tasks = [
    {
        "id": 1,
        "todo_name": "Hacer la compra",
        "completed": True
    },
    {
        "id": 2,
        "todo_name": "Estudiar para el examen",
        "completed": True
    },
    {
        "id": 3,
        "todo_name": "Lavar los platos",
        "completed": True
    },
    {
        "id": 4,
        "todo_name": "Estudiar python",
        "completed": False
    },
]

options = [
    "tasks",
    "add",
    "delete",
    "update",
    "completed",
    "uncompleted",
    "exit"
]


def list_tasks():
    for task in tasks:
        print(
            f"{task['id']}. {task['todo_name']} { '|x|' if task['completed'] else '| |'}")


def add_task():
    name = input("Nombre del todo: ")
    unique_id = tasks[-1]['id'] + 1
    todo = {"id": unique_id, "todo_name": name, "completed": False}
    tasks.append(todo)


def delete_task(todo_id):
    try:  # Convertir la entrada a entero
        todo_index = next(index for (index, task) in enumerate(
            tasks) if task['id'] == todo_id)
        tasks.pop(todo_index)
        print(f"Task with ID {todo_id} deleted successfully.")
    except ValueError:
        print("Please enter a valid number.")
    except StopIteration:
        print(f"Task with ID {todo_id} not found.")


def update_task(todo_id):
    print(todo_id)


def tasks_completed():
    print("Tasks completed", end=" ")
    print("\u2713")

    tasks_check = [task for task in tasks if task['completed'] is True]
    for task in tasks_check:
        print(f"{task['id']}. {task['todo_name']}")


def tasks_uncompleted():
    print("taks uncompleted X")

    tasks_idle = [task for task in tasks if task['completed'] is False]
    for task in tasks_idle:
        print(f"{task['id']}. {task['todo_name']}")


def menu():
    print("="*80)
    print(" | ".join(options))


def start_app():
    print("="*80)
    print("#" * 35, "TODO APP", "#" * 35)
    while True:
        menu()
        option = input("Choose option: ")
        while option not in options:
            print("=" * 80)
            print(" | ".join(options))
            option = input("Try again: ")

        option = option.lower()

        if option == "tasks":
            list_tasks()
        elif option == "add":
            add_task()
        elif option == "delete":
            todo_id = int(input("Select number: "))
            delete_task(todo_id)
        elif option == "update":
            todo_id = int(input("Select number: "))
            update_task(todo_id)
        elif option == "completed":
            tasks_completed()
        elif option == "uncompleted":
            tasks_uncompleted()


start_app()
