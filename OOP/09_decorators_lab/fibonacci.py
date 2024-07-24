class Fibonacci:
    def __init__(self):
        self.cache = {}

    def __call__(self, num):
        if num not in self.cache:
            if num == 0:
                self.cache[0] = 0
            elif num == 1:
                self.cache[1] = 1
            else:
                self.cache[num] = self(num - 1) + self(num - 2)

        return self.cache[num]


fib = Fibonacci()
for i in range(7):
    print(fib(i))

print(fib.cache)