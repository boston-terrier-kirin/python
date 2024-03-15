def get_todos(filepath="todos.txt"):
    """
    Read  text file and return the list of todo items.
    :param filepath:
    :return: todo items
    """
    with open(filepath, "r") as r_file:
        todos_from_file = r_file.readlines()
    return todos_from_file


def save_todos(todos_to_save, filepath="todos.txt"):
    with open("todos.txt", "w") as w_file:
        w_file.writelines(todos_to_save)