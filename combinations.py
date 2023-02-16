# Все возможные комбинации элементов последовательности.

from itertools import combinations
from random import randint

x = [randint(1, 20) for _ in range(5)]

print(x)
print(*[i for i in combinations(x, 2)], sep='\n')
