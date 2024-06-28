import os

extensions = {}
directory = './'

for element in os.listdir(directory):
    file = os.path.join(directory, element)

    if os.path.isfile(file):
        extension = element.split('.')[-1]

        if extension not in extensions:
            extensions[extension] = []
        extensions[extension].append(element)

    else:
        for el in os.listdir(file):
            file_name = os.path.join(file, el)

            if os.path.isfile(file_name):
                extension = el.split('.')[-1]

                if extension not in extensions:
                    extensions[extension] = []
                extensions[extension].append(el)

with open(os.path.join(directory, 'report.txt'), 'w') as output:
    for ext, filenames in sorted(extensions.items()):
        output.write(f'.{ext}\n')

        for filename in sorted(filenames):
            output.write(f'- - - {filename}\n')