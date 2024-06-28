def not_arrived_guests_func(reservation: set, arrived: list):
    return reservation.difference(arrived)


def reservations():
    reservation_set = set()

    for _ in range(int(input())):
        reservation_code = input()

        if len(reservation_code) == 8:
            reservation_set.add(reservation_code)

    return reservation_set


def arrived_guests():
    arrived_guests_list = []

    while True:
        arrived_guest = input()

        if arrived_guest == 'END':
            break

        arrived_guests_list.append(arrived_guest)

    return arrived_guests_list


not_arrived_guests = not_arrived_guests_func(reservations(), arrived_guests())

print(len(not_arrived_guests))
print(*sorted(not_arrived_guests), sep='\n')

# def arrived_guests_data():
#     arrived = []
#
#     while True:
#         data = input()
#
#         if data == 'END':
#             break
#         arrived.append(data)
#
#     return arrived
#
#
# def printing_func(not_arrived_guests):
#     print(len(not_arrived_guests))
#
#     for guest in sorted(not_arrived_guests):
#         print(guest)
#
#
# reservations = {input() for _ in range(int(input()))}
# arrived_guests = arrived_guests_data()
# not_arrived = reservations.difference(arrived_guests)
# printing_func(not_arrived)
