from collections import deque

bullet_price = int(input())
size_of_gun_barrel = int(input())
barrel_size = size_of_gun_barrel

bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])

intelligence_value = int(input())
shots = 0

while bullets and locks:
    bullet = bullets.pop()
    lock = locks.popleft()

    shots += 1
    barrel_size -= 1

    if bullet > lock:
        print('Ping!')
        locks.appendleft(lock)

    elif bullet <= lock:
        print('Bang!')

    if bullets and barrel_size == 0:
        print('Reloading!')
        barrel_size = size_of_gun_barrel

earned_money = intelligence_value - (bullet_price * shots)

if not locks:
    print(f'{len(bullets)} bullets left. Earned ${earned_money}')
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")