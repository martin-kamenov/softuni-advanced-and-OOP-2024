from collections import deque

money = [int(x) for x in input().split()]
food = deque([int(x) for x in input().split()])

eaten_food = 0

while money and food:
    curr_money = money.pop()
    curr_food = food.popleft()

    if curr_money == curr_food:
        eaten_food += 1
    elif curr_money > curr_food:
        curr_money -= curr_food
        if money:
            money[-1] += curr_money
        eaten_food += 1
    # else:
    #     continue
    # The above else is unnecessary as if the above statements are passed the cycle will continue
    # with next iteration.

if eaten_food >= 4:
    print(f'Gluttony of the day! Henry ate {eaten_food} foods.')
elif eaten_food > 0:
    if eaten_food == 1:
        print(f'Henry ate: {eaten_food} food.')
    else:
        print(f'Henry ate: {eaten_food} foods.')
else:
    print('Henry remained hungry. He will try next weekend again.')
