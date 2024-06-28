from collections import deque

players = deque(input().split())
hot_potato_step = int(input())
counter = 0

while len(players) > 1:
    counter += 1
    current_player_name = players.popleft()

    if counter == hot_potato_step:
        print(f'Removed {current_player_name}')
        counter = 0
    else:
        players.append(current_player_name)

print(f'Last is {players[0]}')
