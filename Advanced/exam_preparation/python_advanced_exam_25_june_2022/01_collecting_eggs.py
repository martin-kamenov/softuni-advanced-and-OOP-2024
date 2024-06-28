from collections import deque


eggs_sizes = deque([int(x) for x in input().split(', ')])
paper_sizes = [int(x) for x in input().split(', ')]

boxes = 0
BOX_SIZE = 50

while eggs_sizes and paper_sizes:
    egg = eggs_sizes.popleft()
    paper = paper_sizes.pop()

    if egg <= 0:
        paper_sizes.append(paper)
        continue

    elif egg == 13:
        paper_sizes.append(paper)
        paper_sizes[0], paper_sizes[-1] = paper_sizes[-1], paper_sizes[0]
        continue

    wrapped_egg = egg + paper

    if wrapped_egg <= BOX_SIZE:
        boxes += 1

if not boxes:
    print("Sorry! You couldn't fill any boxes!")
else:
    print(f"Great! You filled {boxes} boxes.")

if eggs_sizes:
    print(f"Eggs left: {', '.join(str(egg) for egg in eggs_sizes)}")
if paper_sizes:
    print(f"Pieces of paper left: {', '.join(str(paper) for paper in paper_sizes)}")
