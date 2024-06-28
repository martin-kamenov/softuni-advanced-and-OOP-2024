import os


def save_extensions(dir_name, first_level=False):
    for filename in os.listdir(dir_name):
        curr_file = os.path.join(dir_name, filename)

        if os.path.isfile(curr_file):
            curr_extension = filename.split('.')[-1]
            extensions[curr_extension] = extensions.get(curr_extension, []) + [filename]

        elif os.path.isdir(curr_file) and not first_level:
            save_extensions(curr_file, first_level=True)


directory = './example'
extensions = {}
result = []

try:
    save_extensions(directory)
except FileNotFoundError:
    print('Directory not found!')

extensions = sorted(extensions.items(), key=lambda kvp: kvp[0])

for extension, files in extensions:
    result.append(f'.{extension}')

    for file in sorted(files):
        result.append(f'- - - {file}')

with open('example/report.txt', 'w') as report_file:
    report_file.write('\n'.join(result))
