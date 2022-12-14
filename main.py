while True:

    # Get user input and strip space characters by choosing a number
    user_actions = input("Type 1 to ADD" + "\n"
                         "Type 2 to SHOW" + "\n"
                         "Type 3 to EDIT" + "\n"
                         "Type 4 to COMPLETE" + "\n"
                         "Type 5 to EXIT ") + "\n"

    user_actions = user_actions.strip()

    match user_actions:
        # Check if user action is "1"
        case '1':  # (Case 1 ADD) will add new things in text file.
            todo = input("Enter a todo: ") + "\n"

            file = open('newArchives.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('newArchives.txt', 'w')
            file.writelines(todos)
            file.close()
        # Check if user action is "2"
        case '2':  # (Case 2 SHOW) will show things that were added in text file.
            file = open('newArchives.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)
        # Check if user action is "3"
        case '3':  # (Case 3 EDIT) will edit after choosing a number.
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo
        case '4':
            number = int(input("Number of the todo to complete"))
            todos.pop(number - 1)
        case '5':
            break

print("Bye!")
