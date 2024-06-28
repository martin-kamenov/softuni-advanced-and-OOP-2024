def printing_func(data):
    if data:
        for car in data:
            print(car)
    else:
        print('Parking Lot is Empty')


PARK_IN = 'IN'
PARK_OUT = 'OUT'
parking = set()

for _ in range(int(input())):
    command, license_plate_number = input().split(', ')

    if command == PARK_IN:
        parking.add(license_plate_number)
    elif command == PARK_OUT:
        parking.remove(license_plate_number)

printing_func(parking)
