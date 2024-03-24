class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()


gen = FirstHundredGenerator()
print(next(gen))
print(next(gen))


class FirstHundredIterable:
    def __iter__(self):
        return FirstHundredGenerator()


print(sum(FirstHundredIterable()))
