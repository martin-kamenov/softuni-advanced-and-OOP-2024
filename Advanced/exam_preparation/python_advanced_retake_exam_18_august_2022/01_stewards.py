from collections import deque

seats_numbers = input().split(', ')
first_sequence = deque([int(x) for x in input().split(', ')])
second_sequence = deque([int(x) for x in input().split(', ')])

TARGETED_SEATS_MATCHES = 3
TOTAL_ROTATIONS = 10

taken_seats = []
rotations = 0

while True:
    if len(taken_seats) == TARGETED_SEATS_MATCHES:
        break

    if rotations == TOTAL_ROTATIONS:
        break

    first_number = first_sequence.popleft()
    second_number = second_sequence.pop()

    ascii_result = chr(first_number + second_number)
    first_match = str(first_number) + ascii_result
    second_match = str(second_number) + ascii_result

    for seat in (first_match, second_match):

        if seat in taken_seats:
            break

        if seat in seats_numbers:
            taken_seats.append(seat)
            seats_numbers.remove(seat)
            break
    else:
        first_sequence.append(first_number)
        second_sequence.appendleft(second_number)
    rotations += 1

print(f'Seat matches: {", ".join(taken_seats)}')
print(f'Rotations count: {rotations}')
