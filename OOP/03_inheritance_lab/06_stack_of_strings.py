from typing import List

class Stack:

    def __init__(self):
        self.data: List[str] = []

    def push(self, element) -> None:
        self.data.append(element)

    def pop(self) -> str:
        return self.data.pop()

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def __str__(self) -> str:
        return "[" + ", ".join(self.data[::-1]) + "]"

s = Stack()

print(s.is_empty())
print(s.data)
s.push('a')
s.push('b')
s.push('c')
s.push('d')
print(s.is_empty())
print(s.data)
print(s.pop())
print(s.top())
print(s)
print(s.is_empty())
print(s.data)
print(s)