from collections import deque

food = int(input())
orders = deque([int(n) for n in input().split()])

print(max(orders))

for order in orders.copy():
    if food - order >= 0:
        orders.popleft()
        food -= order
    else:
        print(f'Orders left: {" ".join(str(s) for s in orders)}')
        break
else:
    print('Orders complete')


# print(sum(int(n) for n in input().split())) # returns sum of numbers


# from collections import deque
#
# food_quantity = int(input())
# orders = deque([int(o) for o in input().split()])
#
# print(max(orders))
#
# while orders:
#
#     order = orders.popleft()
#
#     if food_quantity >= order:
#         food_quantity -= order
#     else:
#         orders.appendleft(order)
#         print(f'Orders left:', *orders, sep=' ')
#         break
# else:
#     print('Orders complete')


# from collections import deque
#
# food = int(input())
# orders = deque([int(x) for x in input().split()])
#
# print(max(orders))
#
# while orders:
#     order = orders.popleft()
#
#     if food >= order:
#         food -= order
#     else:
#         orders.appendleft(order)
#         break
#
# if orders:
#     print(f'Orders left:', *orders)
# else:
#     print('Orders complete')
