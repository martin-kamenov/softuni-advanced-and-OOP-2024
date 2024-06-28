import os

while True:
    command = input()

    if command == 'End':
        break

    action, file, *content = command.split('-')

    if action == 'Create':
        curr_file = open(file, 'w').close()

    elif action == 'Add':
        with open(file, 'a') as file_:
            file_.write(f'{content[0]}\n')

    elif action == 'Replace':
        try:
            with open(file, 'r+') as file_:
                text = file_.read()
                text = text.replace(content[0], content[1])

                file_.seek(0)
                file_.write(text)
                file_.truncate()

        except FileNotFoundError:
            print('An error occurred')

    else:
        try:
            os.remove(file)
        except FileNotFoundError:
            print('An error occurred')
