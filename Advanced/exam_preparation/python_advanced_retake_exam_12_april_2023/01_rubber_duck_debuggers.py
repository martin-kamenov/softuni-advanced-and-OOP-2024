from collections import deque

programmers_time = deque([int(x) for x in input().split()])
number_of_tasks = [int(x) for x in input().split()]

darth_vader_duck = range(0, 61)
thor_ducky = range(61, 121)
big_blue_ducky = range(121, 181)
small_yellow_ducky = range(181, 240)

rubber_ducky_types = {
    'Darth Vader Ducky': 0,
    'Thor Ducky': 0,
    'Big Blue Rubber Ducky': 0,
    'Small Yellow Rubber Ducky': 0
}

while programmers_time and number_of_tasks:
    time = programmers_time.popleft()
    task = number_of_tasks.pop()

    time_needed = time * task

    if time_needed in darth_vader_duck:
        rubber_ducky_types['Darth Vader Ducky'] += 1
    elif time_needed in thor_ducky:
        rubber_ducky_types['Thor Ducky'] += 1
    elif time_needed in big_blue_ducky:
        rubber_ducky_types['Big Blue Rubber Ducky'] += 1
    elif time_needed in small_yellow_ducky:
        rubber_ducky_types['Small Yellow Rubber Ducky'] += 1
    else:
        number_of_tasks.append(task - 2)
        programmers_time.append(time)

else:
    print('Congratulations, all tasks have been completed! Rubber ducks rewarded:')

{print(f'{duck}: {count}') for duck, count in rubber_ducky_types.items()}
