from collections import deque

bowls_of_ramen = [int(x) for x in input().split(', ')]
customers = deque([int(x) for x in input().split(', ')])

while bowls_of_ramen and customers:
    ramen = bowls_of_ramen.pop()
    customer_ = customers.popleft()

    if ramen > customer_:
        ramen -= customer_
        bowls_of_ramen.append(ramen)

    elif ramen < customer_:
        customer_ -= ramen
        customers.appendleft(customer_)

if not customers:
    print('Great job! You served all the customers.')

    if bowls_of_ramen:
        print(f'Bowls of ramen left: {", ".join(str(b) for b in bowls_of_ramen)}')

else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(c) for c in customers)}")
