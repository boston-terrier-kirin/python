import time
from functions import get_todos, save_todos

now = time.strftime("%Y/%m/%d %H:%M:%S")
print(f"It is {now}")

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + "\n")
        save_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()
        new_todos = [item.strip("\n") for item in todos]
        for index, item in enumerate(new_todos):
            print(f"{index + 1}--{item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            save_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number = number - 1

            todos = get_todos()
            todos.pop(number)

            save_todos(todos)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print(f"Invalid command: {user_action}")

print("Bye!")