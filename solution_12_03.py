from string import ascii_letters

data = open('data/data_12_03.txt', 'r').read().split('\n')

priority = 0
for rucksack in data:
    comp1 = set(rucksack[:len(rucksack)//2])
    comp2 = set(rucksack[len(rucksack)//2:])

    item = comp1.intersection(comp2).pop()
    priority += (ascii_letters.index(item) + 1)

print(priority)

####### Part 2
from itertools import islice

priority = 0
for i in range(0, len(data), 3):
    intersect1 = set(data[i]).intersection(set(data[i+1]))
    intersect2 = intersect1.intersection(set(data[i+2]))

    item = intersect2.pop()
    priority += (ascii_letters.index(item) + 1)

print(priority)
