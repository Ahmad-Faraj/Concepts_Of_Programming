import random

random_numbers = [random.randint(1 , 100) for _ in range(30)]

for _ in random_numbers:
    print(_, end=" ")
