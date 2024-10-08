def add_car(iterable, car):
    iterable.add(car)


def remove_car(iterable, car):
    if car in iterable:
        iterable.discard(car)


parking = set()

mapper = {'IN': add_car, 'OUT': remove_car}

for _ in range(int(input())):
    direction, car_number = input().split(', ')
    mapper[direction](parking, car_number)

if parking:
    print(*parking, sep='\n')
else:
    print('Parking Lot is Empty')
