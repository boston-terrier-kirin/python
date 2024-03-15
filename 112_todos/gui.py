import PySimpleGUI as sg
import functions

label = sg.Text("Type in a todo")
input_box = sg.InputText(key="todo", tooltip="Enter todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(key="todos",
                      values=functions.get_todos(),
                      enable_events=True,
                      size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window("Todo App",
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()

    print("event", event)
    print("values", values)

    if event == "Add":
        new_todo = values["todo"] + "\n"
        todos = functions.get_todos()
        todos.append(new_todo)
        functions.save_todos(todos)

        window["todos"].update(values=todos)
    elif event == "Edit":
        todo_to_edit = values["todos"][0]
        new_todo = values["todo"] + "\n"

        todos = functions.get_todos()
        index = todos.index(todo_to_edit)
        todos[index] = new_todo
        functions.save_todos(todos)

        window["todos"].update(values=todos)
    elif event == "todos":
        window["todo"].update(value=values["todos"][0])
    elif event == sg.WINDOW_CLOSED:
        break

window.close()
