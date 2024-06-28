from collections import deque

green_window = int(input())
free_window = int(input())
cars_queue = deque()
passed_cars = 0

while True:

    event = input()

    if event == 'END':
        break

    if not event == 'green':
        cars_queue.append(event)
    else:
        current_green = green_window

        while cars_queue and current_green > 0:
            car = cars_queue.popleft()
            time = current_green + free_window

            if len(car) > time:
                print('A crash happened!')
                print(f"{car} was hit at {car[time]}.")
                raise SystemExit

            current_green -= len(car)
            passed_cars += 1

print("Everyone is safe.")
print(f"{passed_cars} total cars passed the crossroads.")
