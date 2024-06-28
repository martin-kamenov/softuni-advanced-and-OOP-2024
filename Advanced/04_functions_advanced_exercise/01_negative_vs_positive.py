def prin_func(negative, positive):
    print(sum(negative))
    print(sum(positive))

    if abs(sum(negative)) > sum(positive):
        print("The negatives are stronger than the positives")
    elif sum(positive) > abs(sum(negative)):
        print("The positives are stronger than the negatives")


numbers = [int(x) for x in input().split()]
negative_numbers = [x for x in numbers if x < 0]
positive_numbers = [x for x in numbers if x > 0]

prin_func(negative_numbers, positive_numbers)
