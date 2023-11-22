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


def menu():
    print("="*80)
    print("#" * 25, " wELCOME TO MT TODO APP", "#" * 25)
    print("="*80)
    print(" | ".join(options))


def iniciarApp():
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
        print("agregamos tarea")
    elif option == "delete":
        print("eliminamos tarea")
    elif option == "update":
        print("editamos tarea")
    elif option == "completed":
        print("tareas completadas")


iniciarApp()
