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
todo_id = 4

one_element = [task for task in tasks if task['id'] == todo_id][0]

todo_index = tasks.index(one_element)
print(tasks[todo_index])
