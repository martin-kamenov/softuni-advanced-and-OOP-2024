def start_spring(**spring_objects):
    objects = {}
    result = []

    for name, object_type in spring_objects.items():
        if object_type not in objects:
            objects[object_type] = []
        objects[object_type].append(name)

    sorted_objects = sorted(objects.items(), key=lambda x: (-len(x[1]), x[0]))

    for key, values in sorted_objects:
        values.sort()
        result.append(f'{key}:')

        for value in values:
            result.append(f'-{value}')

    return '\n'.join(result)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
