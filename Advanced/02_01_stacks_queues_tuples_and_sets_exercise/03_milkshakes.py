from collections import deque

chocolates = [int(x) for x in input().split(", ")]
cups_of_milk = deque([int(x) for x in input().split(", ")])

milkshakes = 0

while milkshakes != 5 and chocolates and cups_of_milk:
    chocolate = chocolates.pop()
    milk = cups_of_milk.popleft()

    if chocolate <= 0 and milk <= 0:
        continue
    elif chocolate <= 0:
        cups_of_milk.appendleft(milk)
        continue
    elif milk <= 0:
        chocolates.append(chocolate)
        continue

    if milk == chocolate:
        milkshakes += 1
    else:
        chocolates.append(chocolate - 5)
        cups_of_milk.append(milk)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(s) for s in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(s) for s in cups_of_milk) or 'empty'}")

