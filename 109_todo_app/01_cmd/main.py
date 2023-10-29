todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"
            todos.append(todo)

            file = open("todos.txt", "a")
            print(todos)
            file.writelines(todos)
            file.close()
        case "show":
            for index, item in enumerate(todos):
                print(f"{index} - {item}")
        case "edit":
            number = int(input("Number of the todo to edit: "))
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case "complete":
            number = int(input("Number of the todo to complete: "))
            todos.pop(number)
        case "exit":
            break

print("Bye!")
